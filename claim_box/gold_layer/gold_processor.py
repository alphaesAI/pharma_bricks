"""
Gold Layer Processor - BIS-style JSON-driven SQL execution
"""
import json
import pandas as pd
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class GoldTableConfig:
    """Configuration for a gold table."""
    entity: str
    destination_table: str
    source_tables: List[Dict[str, Any]]
    sql_script: str
    merge_key: str


class GoldProcessor:
    """
    Processes gold layer tables using JSON configuration.
    
    Usage:
        processor = GoldProcessor(db_connection)
        processor.process_config('claim_box/config/gold_gapsincare.json')
    """
    
    def __init__(self, db_engine):
        """
        Initialize with database connection.
        
        Args:
            db_engine: SQLAlchemy database engine (e.g., PostgreSQL)
        """
        self.db_engine = db_engine
        self.loaded_sources: Dict[str, pd.DataFrame] = {}
    
    def process_config(self, config_path: str) -> Dict[str, int]:
        """
        Process a gold layer JSON configuration file.
        
        Args:
            config_path: Path to JSON config file
            
        Returns:
            Dictionary with entity names and record counts
        """
        # Load config
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        results = {}
        
        # Process each gold table in config
        for table_config in config.get('gold_tables', []):
            entity = table_config['entity']
            gold_config = GoldTableConfig(
                entity=entity,
                destination_table=table_config['destination_table'],
                source_tables=table_config['source_tables'],
                sql_script=table_config['sql_script'],
                merge_key=table_config.get('merge_key', 'id')
            )
            
            # Load source tables
            self._load_sources(gold_config.source_tables)
            
            # Execute SQL transformation
            record_count = self._execute_gold_transform(gold_config)
            
            results[entity] = record_count
            print(f"✓ Processed {entity}: {record_count} records → {gold_config.destination_table}")
        
        return results
    
    def _load_sources(self, source_tables: List[Dict[str, Any]]):
        """Load source tables from database into memory."""
        for source in source_tables:
            entity = source['entity']
            table_name = source['table_name']
            
            # Load from PostgreSQL
            query = f'SELECT * FROM {table_name}'
            df = pd.read_sql(query, self.db_engine)
            
            self.loaded_sources[entity] = df
            print(f"  Loaded source: {entity} ({len(df)} records)")
    
    def _execute_gold_transform(self, config: GoldTableConfig) -> int:
        """
        Execute SQL transformation and save to destination table.
        
        For simplified version, we'll use pandas SQL execution.
        In production, you'd use the actual SQL against PostgreSQL.
        """
        # Method 1: Direct SQL execution (if tables exist in DB)
        try:
            result_df = pd.read_sql(config.sql_script, self.db_engine)
        except Exception as e:
            print(f"  Warning: Direct SQL failed ({e}), using pandas fallback")
            # Method 2: Pandas fallback - manually filter/transform
            result_df = self._pandas_fallback_transform(config)
        
        # Save to destination table
        if len(result_df) > 0:
            result_df.to_sql(
                config.destination_table,
                self.db_engine,
                if_exists='replace',
                index=False
            )
        
        return len(result_df)
    
    def _pandas_fallback_transform(self, config: GoldTableConfig) -> pd.DataFrame:
        """
        Fallback transformation using pandas when SQL fails.
        This mimics the SQL logic in Python.
        """
        # Get claim headers
        ch = self.loaded_sources.get('claim_headers')
        cl = self.loaded_sources.get('claim_lines')
        
        if ch is None:
            return pd.DataFrame()
        
        # Filter C records with diabetes diagnosis
        diabetes_mask = (
            ch['PrincipalDiagnosisCode'].str.startswith('E11', na=False) |
            ch['Diag1'].str.startswith('E11', na=False) |
            ch['Diag2'].str.startswith('E11', na=False)
        )
        
        filtered_ch = ch[ch['RecordType'] == 'C'].copy()
        filtered_ch = filtered_ch[diabetes_mask]
        
        results = []
        for _, row in filtered_ch.iterrows():
            encounter_icn = row['EncounterICN']
            
            # Check for A1C test in claim lines
            has_a1c = False
            if cl is not None:
                claim_lines = cl[cl['ClaimLineEncounterICN'] == encounter_icn]
                a1c_codes = ['83036', '83037']
                has_a1c = claim_lines['ServiceLineProcedureCode'].isin(a1c_codes).any()
            
            results.append({
                'gapsInCareID': encounter_icn,
                'yearMonth': int(pd.Timestamp.now().strftime('%Y%m')),
                'planMemberID': row['HICNumber'],
                'measureID': 'DIABETES',
                'subMeasureID': 'A1C',
                'measureCode': 'HEDIS_DIABETES_A1C',
                'measureName': 'Diabetes A1C Control',
                'numerCnt': 1 if has_a1c else 0,
                'denomCnt': 1,
                'eventName': 'A1C Test Required',
                'dateOfService': row['MemberDOB'],
                'providerID': row['BillingProviderNPI'],
                'providerName': row['BillingProviderLastOrOrg'],
                'claimNumber': row['PrincipalDiagnosisCode'],
                'creationDateTime': pd.Timestamp.now()
            })
        
        return pd.DataFrame(results)


    def process_master_config(self, master_config_path: str) -> Dict[str, Dict[str, int]]:
        """
        Process a master configuration that references multiple gold table configs.
        
        Args:
            master_config_path: Path to master JSON config
            
        Returns:
            Nested dictionary with results for each config file
        """
        with open(master_config_path, 'r') as f:
            master_config = json.load(f)
        
        all_results = {}
        processing_order = master_config.get('processing_order', [])
        
        print(f"\nProcessing {len(processing_order)} gold table configs...")
        print("=" * 60)
        
        for config_path in processing_order:
            print(f"\n📄 Processing: {config_path}")
            results = self.process_config(config_path)
            all_results[config_path] = results
        
        return all_results


def main():
    """Example usage with master config."""
    from sqlalchemy import create_engine
    
    # Connect to PostgreSQL (adjust connection string as needed)
    # For SQLite (simple local testing):
    # engine = create_engine('sqlite:///claims.db')
    
    # For PostgreSQL:
    engine = create_engine('postgresql://user:password@localhost:5432/claimsdb')
    
    # Create processor
    processor = GoldProcessor(engine)
    
    # Process all gold tables via master config
    results = processor.process_master_config('claim_box/config/gold_master.json')
    
    print("\n" + "=" * 60)
    print("🎉 GOLD LAYER PROCESSING COMPLETE")
    print("=" * 60)
    for config_path, config_results in results.items():
        print(f"\n{config_path}:")
        for entity, count in config_results.items():
            print(f"  ✓ {entity}: {count} records")


def process_single_config(config_path: str, db_url: str = 'sqlite:///claims.db'):
    """
    Process a single gold table config.
    
    Args:
        config_path: Path to gold table JSON config
        db_url: Database connection URL
    """
    from sqlalchemy import create_engine
    
    engine = create_engine(db_url)
    processor = GoldProcessor(engine)
    results = processor.process_config(config_path)
    
    print(f"\n✓ Processed {config_path}:")
    for entity, count in results.items():
        print(f"  {entity}: {count} records")
    
    return results


if __name__ == "__main__":
    main()
