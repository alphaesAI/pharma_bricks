"""
Gold Layer Processing Module

BIS-style JSON-driven gold table and dimension table generation.

Usage:
    from claim_box.gold_layer import GoldProcessor, DimensionProcessor
    
    # Process dimension tables (SCD2)
    dim_processor = DimensionProcessor(db_engine)
    dim_processor.process_config('config/dim_member.json')
    
    # Process gold tables
    gold_processor = GoldProcessor(db_engine)
    gold_processor.process_config('config/gold_gapsincare.json')
"""

from .gold_processor import GoldProcessor, GoldTableConfig, process_single_config
from .dimension_processor import DimensionProcessor, DimensionConfig, process_dimension_config

__all__ = [
    'GoldProcessor', 'GoldTableConfig', 'process_single_config',
    'DimensionProcessor', 'DimensionConfig', 'process_dimension_config'
]
