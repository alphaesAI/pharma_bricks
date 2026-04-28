"""Configurable CSV Extractor for X12 EDI files.
 
Uses JSON configuration to map EDI segments to CSV columns.
No hardcoded segment logic - entirely driven by config.
"""
 
import csv
import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
 
try:
    from pyx12.x12file import X12File
except ImportError:
    X12File = None
 
logger = logging.getLogger(__name__)
 
 
@dataclass
class ExtractionRule:
    """Rule for extracting a single column from EDI segments."""
    name: str
    segment: Optional[str] = None
    element_index: Optional[int] = None
    qualifier: Optional[Dict[str, str]] = None
    sub_delimiter: Optional[str] = None
    sub_index: Optional[int] = None
    data_type: str = "string"
    required: bool = False
    source_type: str = "segment"  # "segment" or "parent_reference"
    parent_field: Optional[str] = None
 
 
@dataclass
class OutputFileConfig:
    """Configuration for one output CSV file."""
    file_name: str
    entity: str
    delimiter: str
    key_field: str
    trigger_segment: str
    columns: List[ExtractionRule]
    parent_key: Optional[str] = None
 
 
class CSVExtractor:
    """Extracts CSV files from X12 EDI using JSON configuration."""
 
    def __init__(self, config_path: Path):
        """Initialize with extraction configuration.
 
        Args:
            config_path: Path to csv_extraction.json
        """
        self.config = self._load_config(config_path)
        self.output_configs = self._parse_configs()
        logger.info(f"CSVExtractor initialized with {len(self.output_configs)} output files")
 
    def _load_config(self, path: Path) -> Dict:
        """Load extraction configuration from JSON."""
        with open(path, 'r') as f:
            return json.load(f)
 
    def _parse_configs(self) -> List[OutputFileConfig]:
        """Parse JSON into OutputFileConfig objects."""
        configs = []
        for file_def in self.config.get("output_files", []):
            columns = []
            for col_def in file_def.get("columns", []):
                source = col_def.get("source", {})
 
                # Determine source type
                source_type = source.get("type", "segment")
 
                rule = ExtractionRule(
                    name=col_def["name"],
                    segment=source.get("segment"),
                    element_index=source.get("element_index"),
                    qualifier=source.get("qualifier"),
                    sub_delimiter=source.get("sub_delimiter"),
                    sub_index=source.get("sub_index"),
                    data_type=source.get("data_type", "string"),
                    required=source.get("required", False),
                    source_type=source_type,
                    parent_field=source.get("field") if source_type == "parent_reference" else None
                )
                columns.append(rule)
 
            config = OutputFileConfig(
                file_name=file_def["file_name"],
                entity=file_def["entity"],
                delimiter=file_def["delimiter"],
                key_field=file_def["key_field"],
                trigger_segment=file_def["trigger_segment"],
                columns=columns,
                parent_key=file_def.get("parent_key")
            )
            configs.append(config)
        return configs
 
    def extract(self, edi_file: Path, output_dir: Path) -> Dict[str, Path]:
        """Extract CSV files from EDI.
 
        Args:
            edi_file: Path to X12 EDI file
            output_dir: Directory to write CSV files
 
        Returns:
            Dictionary mapping entity names to output file paths
        """
        if X12File is None:
            raise ImportError("pyx12 library required")
 
        output_dir.mkdir(parents=True, exist_ok=True)
 
        # Parse EDI into segments
        x12_file = X12File(str(edi_file))
        segments = list(x12_file.segments)
 
        # Process each output file config
        results = {}
        for config in self.output_configs:
            output_path = self._extract_file(segments, config, output_dir)
            results[config.entity] = output_path
            logger.info(f"Extracted {config.entity} to {output_path}")
 
        return results
 
    def _extract_file(self, segments: List[Any], config: OutputFileConfig, output_dir: Path) -> Path:
        """Extract single CSV file based on config."""
        output_path = output_dir / config.file_name
 
        # Collect records
        records = []
        current_parent_values: Dict[str, Any] = {}
        current_record: Dict[str, Any] = {}
        in_record = False
 
        for seg in segments:
            seg_id = getattr(seg, 'seg_id', None)
            elements = getattr(seg, 'elements', [])
 
            # Start new record on trigger segment
            if seg_id == config.trigger_segment:
                # Save previous record if exists
                if in_record and current_record:
                    records.append(current_record)
 
                in_record = True
                current_record = {}
 
                # Extract values for this record
                for rule in config.columns:
                    value = self._extract_value(seg, elements, rule, current_parent_values)
                    if value is not None or rule.required:
                        current_record[rule.name] = value
 
                # Update parent reference values
                if config.key_field in current_record:
                    current_parent_values[config.key_field] = current_record[config.key_field]
 
            # Continue extracting from other segments while in record
            elif in_record and seg_id:
                for rule in config.columns:
                    # Skip if already extracted or if segment doesn't match
                    if rule.source_type != "segment" or rule.segment != seg_id:
                        continue
 
                    # Check qualifier if specified
                    if rule.qualifier:
                        qual_elem = rule.qualifier["element_index"] - 1
                        if qual_elem >= len(elements) or elements[qual_elem] != rule.qualifier["value"]:
                            continue
 
                    # Skip if already has value and not multi-value field
                    if rule.name in current_record and current_record[rule.name]:
                        continue
 
                    value = self._extract_value(seg, elements, rule, current_parent_values)
                    if value is not None:
                        current_record[rule.name] = value
 
            # End of claim/transaction - save record
            if seg_id in ["SE", "CLM"] and seg_id != config.trigger_segment and in_record:
                if current_record:
                    records.append(current_record)
                in_record = False
                current_record = {}
 
        # Don't forget last record
        if in_record and current_record:
            records.append(current_record)
 
        # Write CSV
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=config.delimiter)
 
            # Header
            header = [rule.name for rule in config.columns]
            writer.writerow(header)
 
            # Data rows
            for record in records:
                row = [record.get(rule.name, "") for rule in config.columns]
                writer.writerow(row)
 
        return output_path
 
    def _extract_value(self, seg: Any, elements: List[str], rule: ExtractionRule, parent_values: Dict[str, Any]) -> Optional[str]:
        """Extract value from segment based on rule."""
        # Handle parent reference
        if rule.source_type == "parent_reference":
            return parent_values.get(rule.parent_field, "")
 
        # Check segment match
        if rule.segment and getattr(seg, 'seg_id', None) != rule.segment:
            return None
 
        # Check qualifier
        if rule.qualifier:
            qual_idx = rule.qualifier["element_index"] - 1
            if qual_idx >= len(elements) or elements[qual_idx] != rule.qualifier["value"]:
                return None
 
        # Get element value (convert 1-based to 0-based)
        elem_idx = rule.element_index - 1 if rule.element_index else 0
        if elem_idx >= len(elements):
            return None
 
        value = elements[elem_idx]
 
        # Handle sub-delimiter (e.g., "HC>99213" → split by ">")
        if rule.sub_delimiter and rule.sub_index is not None:
            parts = value.split(rule.sub_delimiter)
            if rule.sub_index < len(parts):
                value = parts[rule.sub_index]
            else:
                return None
 
        return value
 
 
def main():
    """Demo extraction from EDI to CSV."""
    import logging
    logging.basicConfig(level=logging.INFO)
 
    # Paths
    base_dir = Path(__file__).parent.parent
    config_path = base_dir / "config" / "csv_extraction.json"
    edi_file = base_dir / "execution" / "samples" / "837_mult_claims.txt"
    output_dir = base_dir / "output"
 
    # Extract
    extractor = CSVExtractor(config_path)
    results = extractor.extract(edi_file, output_dir)
 
    print("\nExtracted files:")
    for entity, path in results.items():
        print(f"  {entity}: {path}")
 
 
if __name__ == "__main__":
    main()