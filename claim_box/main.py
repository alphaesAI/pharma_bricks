"""
ClaimBox Main Entry Point

Command-line interface for X12 837 EDI parsing and claim extraction.
"""

import argparse
import logging
import json
from pathlib import Path
from typing import Optional
import sys

from claim_box.preprocessing.x12_parser import X12Parser
from claim_box.preprocessing.segment_extractor import SegmentExtractor
from claim_box.preprocessing.claim_builder import ClaimBuilder


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='ClaimBox - X12 837 EDI Parser',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s parse input.edi --output claims.json
  %(prog)s parse input.edi --xml --output intermediate.xml
  %(prog)s parse input.edi --config mappings.json --verbose
        """
    )
    
    parser.add_argument(
        'command',
        choices=['parse'],
        help='Command to execute'
    )
    
    parser.add_argument(
        'input_file',
        type=Path,
        help='Path to X12 837 EDI input file'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output file path (JSON or XML based on options)'
    )
    
    parser.add_argument(
        '-c', '--config',
        type=Path,
        help='Path to configuration JSON file'
    )
    
    parser.add_argument(
        '--xml',
        action='store_true',
        help='Output intermediate XML instead of JSON claims'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    return parser.parse_args()


def process_to_json(input_file: Path, output_file: Optional[Path], config_file: Optional[Path]) -> int:
    """
    Process X12 file to JSON claims.
    
    Args:
        input_file: Path to X12 EDI file
        output_file: Optional output JSON path
        config_file: Optional configuration file
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Initialize components
        parser = X12Parser(config_path=config_file)
        extractor = SegmentExtractor()
        builder = ClaimBuilder()
        
        logging.info(f"Processing {input_file} to JSON format")
        
        # Parse X12 file
        raw_claims = parser.parse(input_file)
        
        # Extract and categorize segments (if using pyx12 segments)
        # Note: This is a simplified flow - in real implementation,
        # we'd extract segments from the X12 file properly
        
        # Build claims
        # For now, using the parser's direct output
        # In full implementation, we'd use:
        # segments_by_loop = extractor.extract_segments(raw_segments)
        # claims = builder.build_claims(segments_by_loop)
        
        # Convert to dict for JSON serialization
        # claims_dict = builder.claims_to_dict(claims)
        claims_dict = raw_claims  # Simplified for now
        
        # Output
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(claims_dict, f, indent=2)
            logging.info(f"Claims written to {output_file}")
        else:
            # Print to stdout
            print(json.dumps(claims_dict, indent=2))
        
        return 0
        
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return 1
    except Exception as e:
        logging.error(f"Processing error: {e}")
        return 1


def process_to_xml(input_file: Path, output_file: Optional[Path], config_file: Optional[Path]) -> int:
    """
    Process X12 file to intermediate XML.
    
    Args:
        input_file: Path to X12 EDI file
        output_file: Optional output XML path
        config_file: Optional configuration file
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        parser = X12Parser(config_path=config_file)
        
        logging.info(f"Processing {input_file} to XML format")
        
        xml_output = parser.parse_to_xml(input_file, output_file)
        
        if not output_file:
            print(xml_output)
        
        return 0
        
    except Exception as e:
        logging.error(f"XML conversion error: {e}")
        return 1


def main() -> int:
    """Main entry point."""
    args = parse_arguments()
    
    setup_logging(args.verbose)
    
    logging.info("ClaimBox X12 Parser Starting")
    
    if not args.input_file.exists():
        logging.error(f"Input file not found: {args.input_file}")
        return 1
    
    if args.xml:
        return process_to_xml(args.input_file, args.output, args.config)
    else:
        return process_to_json(args.input_file, args.output, args.config)


if __name__ == '__main__':
    sys.exit(main())
