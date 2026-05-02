import os
from dataclasses import dataclass
from typing import List


@dataclass
class Segment:
    """Simple container for EDI segment."""
    seg_id: str
    elements: List[str]


class X12Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def __call__(self):
        """
        Reads the file and returns the list of Segment objects.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No file found at {self.file_path}")

        with open(self.file_path, 'r') as f:
            raw_data = f.read().strip()

        return self._parse(raw_data)

    def _parse(self, raw_data):
        """
        Core logic: Manual X12 parsing to ensure correct element splitting.
        """
        segments = []

        # 1. Identify delimiters from the ISA segment
        if len(raw_data) < 106 or not raw_data.startswith('ISA'):
            raise ValueError("Invalid X12 file format.")

        element_sep = raw_data[3]
        segment_sep = raw_data[105]

        # 2. Split into segments
        raw_segments = raw_data.split(segment_sep)

        # 3. Process each segment
        for seg in raw_segments:
            if not seg.strip():
                continue

            parts = seg.split(element_sep)
            tag = parts[0].strip()
            elements = parts[1:]

            segments.append(Segment(seg_id=tag, elements=elements))

        return segments