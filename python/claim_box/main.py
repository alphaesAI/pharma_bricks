"""
ClaimBox Main Entry Point

Simple demonstration of X12 837 EDI preprocessing pipeline.
"""

import logging
import json
from pathlib import Path

from claim_box.preprocessing.x12_parser import X12Parser
from claim_box.preprocessing.segment_extractor import SegmentExtractor
from claim_box.preprocessing.claim_builder import ClaimBuilder


def main():
    """Run the preprocessing pipeline."""
    logging.basicConfig(level=logging.INFO)
    
    # Configuration
    config_path = Path("config/x12_mappings.json")
    input_file = Path("input.edi")
    output_file = Path("output.json")
    
    # Initialize components
    parser = X12Parser(config_path=config_path)
    extractor = SegmentExtractor()
    builder = ClaimBuilder()
    
    # Run pipeline
    logging.info(f"Parsing {input_file}")
    raw_segments = parser.parse(input_file)
    
    logging.info("Extracting segments by loop type")
    segments_by_loop = extractor.extract_segments(raw_segments)
    
    logging.info("Building claims")
    claims = builder.build_claims(segments_by_loop)
    
    # Convert to dict and save
    claims_dict = builder.claims_to_dict(claims)
    
    with open(output_file, 'w') as f:
        json.dump(claims_dict, f, indent=2)
    
    logging.info(f"Output written to {output_file}")


if __name__ == '__main__':
    main()
