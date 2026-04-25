"""
ClaimBox - X12 837 EDI Parser and Claim Processor

A Python/PySpark replacement for BizTalk-based X12 processing.
Local development version for testing before Databricks deployment.

Modules:
    preprocessing: X12 parsing and claim extraction
    config: Field mappings and configurations

Example:
    >>> from claim_box.preprocessing import X12Parser, ClaimBuilder
    >>> parser = X12Parser()
    >>> claims = parser.parse(Path("sample_837.txt"))
"""

__version__ = "0.1.0"
__author__ = "ClaimBox Team"

from claim_box.preprocessing.x12_parser import X12Parser
from claim_box.preprocessing.claim_builder import ClaimBuilder
from claim_box.preprocessing.segment_extractor import SegmentExtractor

__all__ = ["X12Parser", "ClaimBuilder", "SegmentExtractor", "__version__"]
