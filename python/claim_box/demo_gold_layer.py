"""
Demo: Complete Gold Layer Processing Flow

This demonstrates:
1. Load BIS-format CSV into SQLite
2. Run gold layer transformations via JSON configs
3. Output gold_ma_gapsincare, gold_alertgroup, gold_revenuegap tables

No PostgreSQL needed - uses SQLite for easy testing.
"""
import pandas as pd
from sqlalchemy import create_engine
import os
import sys

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from claim_box.gold_layer import GoldProcessor


def load_bis_csv_to_sqlite(csv_path: str, db_path: str = 'claims_demo.db'):
    """
    Load BIS-format CSV into SQLite database.
    Splits C records (headers) and L records (lines) into separate tables.
    """
    print(f"\n📥 Loading {csv_path} into SQLite...")
    
    # Create SQLite engine
    engine = create_engine(f'sqlite:///{db_path}')
    
    # Read BIS-format CSV
    df = pd.read_csv(csv_path, delimiter='|')
    
    # Split into C (headers) and L (lines) records
    df_headers = df[df['RecordType'] == 'C'].copy()
    df_lines = df[df['RecordType'] == 'L'].copy()
    
    # Save to database
    df_headers.to_sql('claim_headers', engine, if_exists='replace', index=False)
    df_lines.to_sql('claim_lines', engine, if_exists='replace', index=False)
    
    print(f"  ✓ Headers (C records): {len(df_headers)} records")
    print(f"  ✓ Lines (L records): {len(df_lines)} records")
    
    return engine


def run_gold_layer(engine, master_config: str = 'claim_box/config/gold_master.json'):
    """
    Run gold layer processing using JSON configs.
    """
    print(f"\n🔧 Running Gold Layer Processing...")
    print("=" * 60)
    
    processor = GoldProcessor(engine)
    results = processor.process_master_config(master_config)
    
    return results


def show_results(engine):
    """
    Display the created gold tables.
    """
    print("\n📊 GOLD LAYER RESULTS")
    print("=" * 60)
    
    # Show gapsincare table
    df_gaps = pd.read_sql("SELECT * FROM gold_ma_gapsincare", engine)
    print(f"\n🩺 gold_ma_gapsincare ({len(df_gaps)} records):")
    if len(df_gaps) > 0:
        print(df_gaps[['gapsInCareID', 'measureCode', 'measureName', 'numerCnt', 'denomCnt']].to_string())
    
    # Show alertgroup table
    df_alerts = pd.read_sql("SELECT * FROM gold_alertgroup", engine)
    print(f"\n🚨 gold_alertgroup ({len(df_alerts)} records):")
    if len(df_alerts) > 0:
        print(df_alerts[['alertGroupID', 'alertGroupCode', 'alertGroupDescription']].to_string())
    
    # Show revenuegap table
    df_revenue = pd.read_sql("SELECT * FROM gold_ma_revenuegap", engine)
    print(f"\n💰 gold_ma_revenuegap ({len(df_revenue)} records):")
    if len(df_revenue) > 0:
        print(df_revenue[['revenueGapID', 'planMemberID', 'totalBilledAmount', 'gapStatus']].to_string())


def main():
    """Run complete demo."""
    # Configuration
    CSV_PATH = 'output/submitted837_outbound.csv'
    DB_PATH = 'claims_demo.db'
    MASTER_CONFIG = 'claim_box/config/gold_master.json'
    
    print("=" * 60)
    print("🏥 BIS-STYLE GOLD LAYER DEMO")
    print("=" * 60)
    
    # Step 1: Load CSV to SQLite
    engine = load_bis_csv_to_sqlite(CSV_PATH, DB_PATH)
    
    # Step 2: Run gold layer processing
    results = run_gold_layer(engine, MASTER_CONFIG)
    
    # Step 3: Show results
    show_results(engine)
    
    print("\n" + "=" * 60)
    print("✅ DEMO COMPLETE")
    print("=" * 60)
    print(f"\nDatabase saved to: {DB_PATH}")
    print("\nGold tables created:")
    for config_path, config_results in results.items():
        for entity, count in config_results.items():
            print(f"  • {entity}: {count} records")
    
    print("\n💡 To add new gold tables:")
    print("  1. Create new JSON config in claim_box/config/gold_<tablename>.json")
    print("  2. Add it to claim_box/config/gold_master.json processing_order")
    print("  3. Run: python claim_box/demo_gold_layer.py")


if __name__ == "__main__":
    main()
