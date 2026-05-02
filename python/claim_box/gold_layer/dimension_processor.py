"""
Dimension Table Processor - BIS-style with SCD Type 2 support

Handles Slowly Changing Dimensions:
- Type 2: Historical tracking (effective dates, isCurrent flag)
- SCD2 merge logic: Close old records, insert new records on changes
"""
import json
import pandas as pd
import hashlib
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from sqlalchemy import text


@dataclass
class DimensionConfig:
    """Configuration for a dimension table."""
    entity: str
    destination_table: str
    source_tables: List[Dict[str, Any]]
    sql_script: str
    merge_key: str
    scd_type: str  # SCD1 or SCD2
    natural_key: str


class DimensionProcessor:
    """
    Processes dimension tables with SCD (Slowly Changing Dimension) support.
    
    BIS-style implementation:
    - SCD2: Tracks history with effectiveStartDate, effectiveEndDate, isCurrent
    - Hash-based change detection (fullRowHash)
    - Automatic expiration of old records on changes
    
    Usage:
        processor = DimensionProcessor(db_engine)
        processor.process_config('claim_box/config/dim_member.json')
    """
    
    def __init__(self, db_engine):
        self.db_engine = db_engine
        self.loaded_sources: Dict[str, pd.DataFrame] = {}
    
    def process_config(self, config_path: str) -> Dict[str, int]:
        """
        Process a dimension table JSON configuration.
        
        Args:
            config_path: Path to JSON config file
            
        Returns:
            Dictionary with entity names and record counts
        """
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        results = {}
        
        for table_config in config.get('dimension_tables', []):
            entity = table_config['entity']
            dim_config = DimensionConfig(
                entity=entity,
                destination_table=table_config['destination_table'],
                source_tables=table_config['source_tables'],
                sql_script=table_config['sql_script'],
                merge_key=table_config['merge_key'],
                scd_type=table_config.get('scd_type', 'SCD1'),
                natural_key=table_config.get('natural_key', table_config['merge_key'])
            )
            
            # Load source tables
            self._load_sources(dim_config.source_tables)
            
            # Execute dimension transform with SCD logic
            record_count = self._execute_dimension_transform(dim_config)
            
            results[entity] = record_count
            print(f"✓ Processed {entity}: {record_count} records → {dim_config.destination_table}")
        
        return results
    
    def _load_sources(self, source_tables: List[Dict[str, Any]]):
        """Load source tables from database into memory."""
        for source in source_tables:
            entity = source['entity']
            table_name = source['table_name']
            
            query = f'SELECT * FROM {table_name}'
            df = pd.read_sql(query, self.db_engine)
            
            self.loaded_sources[entity] = df
            print(f"  Loaded source: {entity} ({len(df)} records)")
    
    def _execute_dimension_transform(self, config: DimensionConfig) -> int:
        """
        Execute dimension transformation with SCD logic.
        
        For SCD2:
        1. Get new data from source
        2. Calculate row hashes
        3. Compare with existing current records
        4. Close changed records (set isCurrent=0, effectiveEndDate=current_date)
        5. Insert new records with isCurrent=1
        """
        # Get new data from SQL
        try:
            new_data = pd.read_sql(config.sql_script, self.db_engine)
        except Exception as e:
            print(f"  Warning: Direct SQL failed ({e}), using pandas fallback")
            new_data = self._pandas_fallback_transform(config)
        
        if new_data.empty:
            return 0
        
        # Calculate hash for change detection
        new_data = self._calculate_row_hashes(new_data)
        
        if config.scd_type == 'SCD2':
            return self._apply_scd2_logic(config, new_data)
        else:
            # SCD1: Simple upsert (overwrite)
            return self._apply_scd1_logic(config, new_data)
    
    def _calculate_row_hashes(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate MD5 hash of concatenated row values for change detection.
        BIS-style hash implementation.
        """
        def hash_row(row):
            # Concatenate all non-null values with delimiter
            values = []
            for col in df.columns:
                if col not in ['createdDateTime', 'updatedDateTime', 'fullRowHash', 
                               'effectiveStartDate', 'effectiveEndDate', 'isCurrent', 
                               'memberKey', 'providerKey']:
                    val = row.get(col, '')
                    if pd.notna(val):
                        values.append(str(val))
            
            # Create hash
            concat_str = '|'.join(values)
            return hashlib.md5(concat_str.encode()).hexdigest()
        
        df['fullRowHash'] = df.apply(hash_row, axis=1)
        return df
    
    def _apply_scd2_logic(self, config: DimensionConfig, new_data: pd.DataFrame) -> int:
        """
        Apply SCD Type 2 logic:
        - Keep history
        - Expire old records on change
        - Insert new current records
        """
        natural_key = config.natural_key
        dest_table = config.destination_table
        
        # Check for existing current records
        existing_query = f"""
            SELECT * FROM {dest_table} 
            WHERE isCurrent = TRUE
        """
        
        try:
            existing = pd.read_sql(existing_query, self.db_engine)
        except:
            existing = pd.DataFrame()
        
        records_to_insert = []
        records_to_update = []
        
        if existing.empty:
            # First load - insert all with isCurrent=1
            new_data['isCurrent'] = True
            new_data['effectiveStartDate'] = pd.Timestamp.now().date()
            new_data['effectiveEndDate'] = None
            new_data['createdDateTime'] = pd.Timestamp.now()
            new_data['updatedDateTime'] = pd.Timestamp.now()
            records_to_insert = new_data.to_dict('records')
        else:
            # Compare and apply SCD2
            for _, new_row in new_data.iterrows():
                nat_key_val = new_row[natural_key]
                new_hash = new_row['fullRowHash']
                
                # Find matching existing record
                match = existing[existing[natural_key] == nat_key_val]
                
                if match.empty:
                    # New record - insert with isCurrent=1
                    new_row_dict = new_row.to_dict()
                    new_row_dict['isCurrent'] = True
                    new_row_dict['effectiveStartDate'] = pd.Timestamp.now().date()
                    new_row_dict['effectiveEndDate'] = None
                    new_row_dict['createdDateTime'] = pd.Timestamp.now()
                    new_row_dict['updatedDateTime'] = pd.Timestamp.now()
                    records_to_insert.append(new_row_dict)
                else:
                    # Existing record - check if changed
                    existing_hash = match.iloc[0]['fullRowHash']
                    if new_hash != existing_hash:
                        # Record changed - need to expire old and insert new
                        records_to_update.append({
                            natural_key: nat_key_val,
                            'effectiveEndDate': pd.Timestamp.now().date(),
                            'isCurrent': False
                        })
                        
                        # Insert new current record
                        new_row_dict = new_row.to_dict()
                        new_row_dict['isCurrent'] = True
                        new_row_dict['effectiveStartDate'] = pd.Timestamp.now().date()
                        new_row_dict['effectiveEndDate'] = None
                        new_row_dict['createdDateTime'] = pd.Timestamp.now()
                        new_row_dict['updatedDateTime'] = pd.Timestamp.now()
                        records_to_insert.append(new_row_dict)
        
        # Execute database operations
        with self.db_engine.connect() as conn:
            # Update expired records
            for upd in records_to_update:
                update_sql = f"""
                    UPDATE {dest_table} 
                    SET effectiveEndDate = :effectiveEndDate,
                        isCurrent = :isCurrent,
                        updatedDateTime = CURRENT_TIMESTAMP
                    WHERE {natural_key} = :{natural_key}
                    AND isCurrent = TRUE
                """
                conn.execute(text(update_sql), upd)
            
            # Insert new records
            if records_to_insert:
                insert_df = pd.DataFrame(records_to_insert)
                insert_df.to_sql(dest_table, conn, if_exists='append', index=False)
            
            conn.commit()
        
        return len(records_to_insert)
    
    def _apply_scd1_logic(self, config: DimensionConfig, new_data: pd.DataFrame) -> int:
        """
        Apply SCD Type 1 logic:
        - No history
        - Overwrite existing records
        """
        # Simple replace for SCD1
        new_data.to_sql(
            config.destination_table,
            self.db_engine,
            if_exists='replace',
            index=False
        )
        return len(new_data)
    
    def _pandas_fallback_transform(self, config: DimensionConfig) -> pd.DataFrame:
        """Fallback transformation using pandas when SQL fails."""
        # This would be implemented similarly to GoldProcessor
        # For now, return empty DataFrame
        return pd.DataFrame()


def process_dimension_config(config_path: str, db_url: str = 'sqlite:///claims.db'):
    """
    Process a single dimension table config.
    
    Args:
        config_path: Path to dimension table JSON config
        db_url: Database connection URL
    """
    from sqlalchemy import create_engine
    
    engine = create_engine(db_url)
    processor = DimensionProcessor(engine)
    results = processor.process_config(config_path)
    
    print(f"\n✓ Processed {config_path}:")
    for entity, count in results.items():
        print(f"  {entity}: {count} records")
    
    return results
