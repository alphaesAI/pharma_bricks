"""
Parser Interface Module

Defines the abstract base interface for X12 parsers.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Any, Optional


class ParserInterface(ABC):
    """Abstract base for X12 parsers."""
    
    @abstractmethod
    def parse(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse X12 file and return list of claims."""
        pass
    
    @abstractmethod
    def parse_to_xml(self, file_path: Path, output_path: Optional[Path] = None) -> str:
        """Parse X12 file to XML format."""
        pass
