import csv
import json
import os
from dataclasses import dataclass
from typing import List, Dict, Any, Optional


@dataclass
class Segment:
    """Simple container for EDI segment."""
    seg_id: str
    elements: List[str]


class CSVWriter:
    def __init__(self, config_path: str, output_dir: str):
        self.config_path = config_path
        self.output_dir = output_dir
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load extraction configuration from JSON."""
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def __call__(self, segments: List[Segment]):
        """
        Process segments and write CSV files based on config.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for file_config in self.config.get("output_files", []):
            self._write_csv(segments, file_config)

    def _write_csv(self, segments: List[Segment], file_config: Dict):
        """Write single CSV file based on configuration."""
        file_name = file_config["file_name"]
        delimiter = file_config.get("delimiter", "|")
        output_path = os.path.join(self.output_dir, file_name)

        # Check if BIS format (multiple record types)
        if "formats" in file_config:
            self._write_bis_format(segments, file_config, output_path, delimiter)
        else:
            # Legacy format - single record type
            trigger = file_config["trigger_segment"]
            columns = file_config["columns"]
            key_field = file_config.get("key_field")
            records = self._extract_records(segments, trigger, columns, key_field)

            # Write CSV
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=delimiter)

                # Header
                header = [col["name"] for col in columns]
                writer.writerow(header)

                # Data rows
                for record in records:
                    row = [record.get(col["name"], "") for col in columns]
                    writer.writerow(row)

            print(f"Written: {output_path} ({len(records)} records)")

    def _write_bis_format(self, segments: List[Segment], file_config: Dict, output_path: str, delimiter: str):
        """Write BIS format CSV with C/L record types."""
        formats = file_config["formats"]
        all_columns = []

        # Collect all unique columns from both formats
        seen_cols = set()
        for fmt in formats:
            for col in fmt["columns"]:
                if col["name"] not in seen_cols:
                    seen_cols.add(col["name"])
                    all_columns.append(col)

        records = []
        parent_values = {}
        pending_segments = []
        current_claim_segments = []
        in_claim = False

        for seg in segments:
            # Cache pre-claim segments
            if not in_claim and seg.seg_id in ["NM1", "DMG", "DTP", "N3", "N4", "REF", "HI"]:
                pending_segments.append(seg)
                continue

            # Start claim on CLM
            if seg.seg_id == "CLM":
                if in_claim:
                    # Process previous claim
                    claim_records = self._process_bis_claim(current_claim_segments, formats, parent_values, pending_segments)
                    records.extend(claim_records)
                    pending_segments = []

                in_claim = True
                current_claim_segments = [seg]
                parent_values = {"claim_id": seg.elements[0], "EncounterICN": seg.elements[0]}
                continue

            if in_claim:
                current_claim_segments.append(seg)

                # End claim on SE
                if seg.seg_id == "SE":
                    claim_records = self._process_bis_claim(current_claim_segments, formats, parent_values, pending_segments)
                    records.extend(claim_records)
                    in_claim = False
                    current_claim_segments = []
                    pending_segments = []

        # Process final claim if any
        if in_claim and current_claim_segments:
            claim_records = self._process_bis_claim(current_claim_segments, formats, parent_values, pending_segments)
            records.extend(claim_records)

        # Write CSV
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=delimiter)

            # Header
            header = [col["name"] for col in all_columns]
            writer.writerow(header)

            # Data rows - ensure all columns present
            for record in records:
                row = [record.get(col["name"], "") for col in all_columns]
                writer.writerow(row)

        print(f"Written: {output_path} ({len(records)} records)")

    def _process_bis_claim(self, claim_segments: List[Segment], formats: List[Dict], parent_values: Dict, pending_segments: List[Segment]) -> List[Dict]:
        """Process a single claim and generate C/L records."""
        records = []

        for fmt in formats:
            trigger = fmt["trigger_segment"]
            columns = fmt["columns"]
            record_type = fmt["record_type"]

            # Find all trigger segments in this claim
            trigger_indices = [i for i, seg in enumerate(claim_segments) if seg.seg_id == trigger]

            for trigger_idx in trigger_indices:
                record = {}

                # Extract from cached pending segments first
                for pending_seg in pending_segments:
                    for col in columns:
                        value = self._extract_column_value(pending_seg, col, parent_values)
                        if value is not None:
                            record[col["name"]] = value

                # Extract from trigger segment
                trigger_seg = claim_segments[trigger_idx]
                for col in columns:
                    value = self._extract_column_value(trigger_seg, col, parent_values)
                    if value is not None:
                        record[col["name"]] = value

                # Continue extracting until next trigger or end
                for i in range(trigger_idx + 1, len(claim_segments)):
                    seg = claim_segments[i]

                    # Stop if we hit another trigger of same type
                    if seg.seg_id == trigger:
                        break

                    # Stop if we hit SE (end)
                    if seg.seg_id == "SE":
                        break

                    for col in columns:
                        if col["name"] in record:
                            continue
                        value = self._extract_column_value(seg, col, parent_values)
                        if value is not None:
                            record[col["name"]] = value

                if record:
                    records.append(record)

        return records

    def _extract_records(self, segments: List[Segment], trigger: str, columns: List[Dict], key_field: str = None) -> List[Dict]:
        """Extract records from segments based on trigger and column rules."""
        records = []
        current_record: Dict[str, Any] = {}
        parent_values: Dict[str, str] = {}
        pending_segments: List[Segment] = []  # Cache segments before trigger
        in_record = False
        debug_mode = False

        for seg in segments:
            # Cache NM1/DMG segments before we hit the trigger
            if not in_record and seg.seg_id in ["NM1", "DMG", "DTP", "N3", "N4", "REF", "HI"]:
                pending_segments.append(seg)
                continue

            # Capture parent values from CLM segment (claim ID)
            if seg.seg_id == "CLM" and len(seg.elements) > 0:
                parent_values["claim_id"] = seg.elements[0]
                parent_values["EncounterICN"] = seg.elements[0]

            # Start new record on trigger segment
            if seg.seg_id == trigger:
                if in_record and current_record:
                    records.append(current_record)

                in_record = True
                current_record = {}

                # First, extract from cached segments (patient, subscriber, etc.)
                for pending_seg in pending_segments:
                    for col in columns:
                        value = self._extract_column_value(pending_seg, col, parent_values)
                        if value is not None:
                            current_record[col["name"]] = value

                # Clear cache for next claim
                pending_segments = []

                # Extract from trigger segment itself
                for col in columns:
                    value = self._extract_column_value(seg, col, parent_values)
                    if value is not None:
                        current_record[col["name"]] = value

            # Continue extracting from other segments while in record
            elif in_record:
                for col in columns:
                    # Skip if already extracted
                    if col["name"] in current_record:
                        continue

                    value = self._extract_column_value(seg, col, parent_values)
                    if value is not None:
                        current_record[col["name"]] = value

            # End record on SE (transaction end)
            if seg.seg_id == "SE" and in_record:
                if current_record:
                    records.append(current_record)
                in_record = False
                current_record = {}

        # Don't forget last record
        if in_record and current_record:
            records.append(current_record)

        return records

    def _extract_column_value(self, seg: Segment, col: Dict, parent_values: Dict[str, str]) -> Optional[str]:
        """Extract value for a single column from segment."""
        source = col.get("source", {})

        # Handle constant values (e.g., RecordType = "C")
        if source.get("type") == "constant":
            return source.get("value")

        # Handle parent reference (e.g., claim ID in line records)
        if source.get("type") == "parent_reference":
            field = source.get("field", "claim_id")
            return parent_values.get(field)

        # Check segment match
        if source.get("segment") != seg.seg_id:
            return None

        # Check context for N3/N4 segments
        if "context" in source:
            # Context matching requires additional logic - simplified here
            # For now, extract if segment matches
            pass

        # Check qualifier if specified
        if "qualifier" in source:
            qual_idx = source["qualifier"]["element_index"] - 1
            qual_val = source["qualifier"]["value"]
            if qual_idx >= len(seg.elements) or seg.elements[qual_idx] != qual_val:
                return None

        return self._extract_value(seg, source)

    def _extract_value(self, seg: Segment, source: Dict) -> Optional[str]:
        """Extract value from segment based on source configuration."""
        elem_idx = source.get("element_index", 1) - 1

        if elem_idx >= len(seg.elements):
            return None

        value = seg.elements[elem_idx]

        # Handle sub-delimiter (e.g., "HC>99213" split by ">")
        if "sub_delimiter" in source and "sub_index" in source:
            parts = value.split(source["sub_delimiter"])
            sub_idx = source["sub_index"]
            if sub_idx < len(parts):
                value = parts[sub_idx]
            else:
                return None

        return value
