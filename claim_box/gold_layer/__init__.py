"""
Gold Layer Processing Module

BIS-style JSON-driven gold table generation.

Usage:
    from claim_box.gold_layer import GoldProcessor
    
    processor = GoldProcessor(db_engine)
    results = processor.process_master_config('config/gold_master.json')
"""

from .gold_processor import GoldProcessor, GoldTableConfig, process_single_config

__all__ = ['GoldProcessor', 'GoldTableConfig', 'process_single_config']
