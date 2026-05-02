#!/usr/bin/env python3
"""
Complete BIS-Style Pipeline Execution

Executes the full data flow:
1. Load BIS-format CSV into PostgreSQL (Bronze layer)
2. Create/Update Dimension Tables (Platinum - SCD2)
3. Create/Update Gold Tables (with foreign keys to dimensions)
4. (Optional) Create Platinum Fact Tables

Usage:
    python claim_box/run_complete_pipeline.py
    
Requirements:
    - PostgreSQL running locally or accessible
    - SQLAlchemy installed
    - BIS-format CSV at output/submitted837_outbound.csv
"""
import os
import sys
import argparse
from pathlib import Path

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy import create_engine, text

from claim_box.gold_layer.dimension_processor import DimensionProcessor
from claim_box.gold_layer.gold_processor import GoldProcessor


class BISPipelineRunner:
    """
    Orchestrates the complete BIS-style data pipeline.
    
    Layer execution order:
    1. Bronze: Load raw CSV data
    2. Platinum Dimensions: Create/update dimMember, dimProvider
    3. Gold Facts: Create gapsincare, revenuegap with foreign keys
    4. Platinum Facts: (Optional) Joined views
    """
    
    def __init__(self, db_url: str, csv_path: str = 'output/submitted837_outbound.csv'):
        """
        Initialize pipeline runner.
        
        Args:
            db_url: PostgreSQL connection URL
                   Example: 'postgresql://user:pass@localhost:5432/claimsdb'
            csv_path: Path to BIS-format CSV file
        """
        self.db_url = db_url
        self.csv_path = csv_path
        self.engine = create_engine(db_url)
        
        # Ensure output directory exists
        Path('output').mkdir(exist_ok=True)
        
        print(f"=" * 70)
        print(f"BIS-STYLE COMPLETE DATA PIPELINE")
        print(f"=" * 70)
        print(f"Database: {db_url}")
        print(f"CSV Source: {csv_path}")
        print(f"=" * 70)
    
    def run_all(self) -> dict:
        """
        Execute complete pipeline in correct order.
        
        Returns:
            Dictionary with results from each layer
        """
        results = {
            'bronze': {},
            'platinum_dimensions': {},
            'gold': {},
            'platinum_facts': {}
        }
        
        # Phase 1: Bronze - Load raw CSV
        print("\nPHASE 1: BRONZE LAYER - Loading CSV Data")
        print("-" * 70)
        results['bronze'] = self._load_bronze_layer()
        
        # Phase 2: Platinum Dimensions - SCD2 processing
        print("\nPHASE 2: PLATINUM DIMENSIONS - Member & Provider")
        print("-" * 70)
        results['platinum_dimensions'] = self._create_dimension_tables()
        
        # Phase 3: Gold Facts - Analytics tables with FKs
        print("\nPHASE 3: GOLD LAYER - Fact Tables")
        print("-" * 70)
        results['gold'] = self._create_gold_tables()
        
        # Phase 4: Platinum Facts - Joined views (optional)
        print("\nPHASE 4: PLATINUM FACTS - Enjoined Views")
        print("-" * 70)
        results['platinum_facts'] = self._create_platinum_facts()
        
        # Summary
        self._print_summary(results)
        
        return results
    
    def _load_bronze_layer(self) -> dict:
        """
        Load BIS-format CSV into PostgreSQL.
        Splits into claim_headers (C records) and claim_lines (L records).
        """
        print(f"Loading {self.csv_path}...")
        
        # Read CSV
        df = pd.read_csv(self.csv_path, delimiter='|', dtype=str)
        
        # Split records
        df_headers = df[df['RecordType'] == 'C'].copy()
        df_lines = df[df['RecordType'] == 'L'].copy()
        
        # Load to database
        df_headers.to_sql('claim_headers', self.engine, if_exists='replace', index=False)
        df_lines.to_sql('claim_lines', self.engine, if_exists='replace', index=False)
        
        # Create indexes for performance
        with self.engine.connect() as conn:
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_ch_icn ON claim_headers(\"EncounterICN\")"))
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_ch_hicn ON claim_headers(\"HICNumber\")"))
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_cl_icn ON claim_lines(\"ClaimLineEncounterICN\")"))
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_cl_proccode ON claim_lines(\"ServiceLineProcedureCode\")"))
            conn.commit()
        
        print(f"  ✓ Headers (C records): {len(df_headers)} records → claim_headers")
        print(f"  ✓ Lines (L records): {len(df_lines)} records → claim_lines")
        
        return {
            'headers': len(df_headers),
            'lines': len(df_lines),
            'total': len(df)
        }
    
    def _create_dimension_tables(self) -> dict:
        """
        Create/Update dimension tables with SCD2 logic.
        """
        results = {}
        
        # Initialize schema first
        self._initialize_dimension_schema()
        
        # Process dimension configs
        dim_configs = [
            ('claim_box/config/dim_member.json', 'dimMember'),
            ('claim_box/config/dim_provider.json', 'dimProvider')
        ]
        
        processor = DimensionProcessor(self.engine)
        
        for config_path, entity_name in dim_configs:
            if os.path.exists(config_path):
                print(f"\nProcessing {entity_name}...")
                dim_results = processor.process_config(config_path)
                results.update(dim_results)
            else:
                print(f"  ⚠ Config not found: {config_path}")
        
        return results
    
    def _initialize_dimension_schema(self):
        """Create dimension tables if they don't exist."""
        schema_files = [
            'claim_box/schemas/platinum_dimmember.sql',
            'claim_box/schemas/platinum_dimprovider.sql'
        ]
        
        with self.engine.connect() as conn:
            for schema_file in schema_files:
                if os.path.exists(schema_file):
                    with open(schema_file, 'r') as f:
                        sql = f.read()
                        # Execute each statement separately
                        for statement in sql.split(';'):
                            if statement.strip():
                                try:
                                    conn.execute(text(statement))
                                except Exception as e:
                                    # Table may already exist, that's OK
                                    if 'already exists' not in str(e).lower():
                                        print(f"  Note: {e}")
            conn.commit()
        
        print("  ✓ Dimension table schemas initialized")
    
    def _create_gold_tables(self) -> dict:
        """
        Create Gold layer fact tables with foreign keys to dimensions.
        """
        results = {}
        
        gold_configs = [
            ('claim_box/config/gold_gapsincare_v2.json', 'gapsincare'),
            ('claim_box/config/gold_revenuegap_v2.json', 'revenuegap'),
            ('claim_box/config/gold_alertgroup.json', 'alertgroup')
        ]
        
        processor = GoldProcessor(self.engine)
        
        for config_path, entity_name in gold_configs:
            if os.path.exists(config_path):
                print(f"\nProcessing {entity_name}...")
                gold_results = processor.process_config(config_path)
                results.update(gold_results)
            else:
                print(f"  ⚠ Config not found: {config_path}")
        
        return results
    
    def _create_platinum_facts(self) -> dict:
        """
        Create Platinum layer fact views with joined dimension data.
        This is optional and creates convenient views for reporting.
        """
        results = {}
        
        # Create a joined view for gaps in care with member/provider details
        view_sql = """
            CREATE OR REPLACE VIEW platinum_fact_gapsincare AS
            SELECT 
                g.gapsInCareID,
                g.yearMonth,
                g.measureCode,
                g.measureName,
                g.numerCnt,
                g.denomCnt,
                m.lastName as memberLastName,
                m.firstName as memberFirstName,
                m.dateofBirth as memberDOB,
                m.gender as memberGender,
                p.lastName as providerLastName,
                p.firstName as providerFirstName,
                p.npi as providerNPI,
                g.eventName,
                g.dateOfService
            FROM gold_ma_gapsincare g
            LEFT JOIN platinum_dimmember m ON g.memberKey = m.memberKey
            LEFT JOIN platinum_dimprovider p ON g.providerKey = p.providerKey
        """
        
        try:
            with self.engine.connect() as conn:
                conn.execute(text(view_sql))
                conn.commit()
            
            # Count records in view
            count_df = pd.read_sql("SELECT COUNT(*) as cnt FROM platinum_fact_gapsincare", self.engine)
            record_count = count_df.iloc[0]['cnt']
            
            print(f"  ✓ Created view: platinum_fact_gapsincare ({record_count} records)")
            results['fact_gapsincare_view'] = record_count
            
        except Exception as e:
            print(f"  ⚠ Could not create platinum view: {e}")
        
        return results
    
    def _print_summary(self, results: dict):
        """Print execution summary."""
        print("\n" + "=" * 70)
        print("PIPELINE EXECUTION COMPLETE")
        print("=" * 70)
        
        print("\nBRONZE LAYER (Raw Data):")
        for key, value in results['bronze'].items():
            print(f"  • {key}: {value} records")
        
        print("\nPLATINUM DIMENSIONS (Lookup Tables):")
        for key, value in results['platinum_dimensions'].items():
            print(f"  • {key}: {value} records")
        
        print("\nGOLD LAYER (Analytics):")
        for key, value in results['gold'].items():
            print(f"  • {key}: {value} records")
        
        print("\nPLATINUM FACTS (Joined Views):")
        for key, value in results['platinum_facts'].items():
            print(f"  • {key}: {value} records")
        
        print("\n" + "=" * 70)
        print("Next steps:")
        print("  1. Query gold tables: SELECT * FROM gold_ma_gapsincare")
        print("  2. Query dimension tables: SELECT * FROM platinum_dimmember")
        print("  3. Query joined view: SELECT * FROM platinum_fact_gapsincare")
        print("=" * 70)


def main():
    """Main entry point with CLI arguments."""
    parser = argparse.ArgumentParser(
        description='Complete BIS-Style Data Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Run with default SQLite (for testing)
    python claim_box/run_complete_pipeline.py
    
    # Run with PostgreSQL
    python claim_box/run_complete_pipeline.py --db-url "postgresql://user:pass@localhost/claimsdb"
    
    # Run with custom CSV
    python claim_box/run_complete_pipeline.py --csv-path "custom/output.csv"
        """
    )
    
    parser.add_argument(
        '--db-url',
        type=str,
        default='sqlite:///claims_pipeline.db',
        help='Database connection URL (default: sqlite:///claims_pipeline.db)'
    )
    
    parser.add_argument(
        '--csv-path',
        type=str,
        default='output/submitted837_outbound.csv',
        help='Path to BIS-format CSV file'
    )
    
    parser.add_argument(
        '--phase',
        type=str,
        choices=['bronze', 'dimensions', 'gold', 'platinum', 'all'],
        default='all',
        help='Run specific phase only (default: all)'
    )
    
    args = parser.parse_args()
    
    # Check if CSV exists
    if not os.path.exists(args.csv_path):
        print(f"Error: CSV file not found: {args.csv_path}")
        print("\nRun the EDI to CSV conversion first:")
        print("  python -m claim_box.consolidation.orchestrator")
        sys.exit(1)
    
    # Run pipeline
    runner = BISPipelineRunner(args.db_url, args.csv_path)
    
    if args.phase == 'all':
        runner.run_all()
    elif args.phase == 'bronze':
        runner._load_bronze_layer()
    elif args.phase == 'dimensions':
        runner._create_dimension_tables()
    elif args.phase == 'gold':
        runner._create_gold_tables()
    elif args.phase == 'platinum':
        runner._create_platinum_facts()


if __name__ == "__main__":
    main()
