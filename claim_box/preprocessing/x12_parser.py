"""
X12 Parser Module

Parses X12 837 EDI files into structured claim data.
Uses pyx12 library for low-level X12 parsing.
"""

import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
import json

try:
    from pyx12.x12file import X12File
    from pyx12.x12xml import X12Xml
except ImportError:
    raise ImportError("pyx12 library required. Install: pip install pyx12")


# Configure logging
logger = logging.getLogger(__name__)


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


class X12Parser(ParserInterface):
    """
    X12 837 Parser implementation.
    
    Responsibilities:
    - Read X12 EDI files
    - Convert to XML (optional intermediate)
    - Extract structured claim data
    """
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize parser with optional configuration.
        
        Args:
            config_path: Path to field mappings JSON configuration
        """
        self.config_path = config_path
        self.config = self._load_config() if config_path else {}
        logger.info(f"X12Parser initialized with config: {config_path}")
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file not found: {self.config_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config: {e}")
            return {}
    
    def parse(self, file_path: Path) -> List[Dict[str, Any]]:
        """
        Parse X12 file and extract claims.
        
        Args:
            file_path: Path to X12 EDI file
            
        Returns:
            List of claim dictionaries
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is not valid X12
        """
        try:
            if not file_path.exists():
                raise FileNotFoundError(f"X12 file not found: {file_path}")
            
            logger.info(f"Parsing X12 file: {file_path}")
            
            # Use pyx12 to parse file
            x12_file = X12File(str(file_path))
            claims = []
            
            # Extract claims from segments
            for segment in x12_file.segments:
                claim_data = self._extract_claim_data(segment)
                if claim_data:
                    claims.append(claim_data)
            
            logger.info(f"Extracted {len(claims)} claims from {file_path}")
            return claims
            
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error parsing X12 file: {e}")
            raise ValueError(f"Failed to parse X12 file: {e}")
    
    def parse_to_xml(self, file_path: Path, output_path: Optional[Path] = None) -> str:
        """
        Parse X12 to XML format.
        
        Args:
            file_path: Path to X12 EDI file
            output_path: Optional path to save XML output
            
        Returns:
            XML string representation of X12
        """
        try:
            if not file_path.exists():
                raise FileNotFoundError(f"X12 file not found: {file_path}")
            
            logger.info(f"Converting X12 to XML: {file_path}")
            
            # Use pyx12 X12Xml converter
            x12_xml = X12Xml()
            xml_output = x12_xml.convert(str(file_path))
            
            if output_path:
                with open(output_path, 'w') as f:
                    f.write(xml_output)
                logger.info(f"XML saved to: {output_path}")
            
            return xml_output
            
        except Exception as e:
            logger.error(f"Error converting to XML: {e}")
            raise ValueError(f"Failed to convert X12 to XML: {e}")
    
    def _extract_claim_data(self, segment: Any) -> Optional[Dict[str, Any]]:
        """
        Extract claim data from a segment.
        
        Args:
            segment: X12 segment from pyx12
            
        Returns:
            Dictionary of claim data or None if not a claim segment
        """
        # This will be implemented based on segment type
        # ST = Transaction Set Header (start of claim)
        # CLM = Claim information
        # NM1 = Name (provider, subscriber, patient)
        # DTM = Date
        
        segment_id = getattr(segment, 'seg_id', None)
        
        if segment_id == 'CLM':
            return self._parse_clm_segment(segment)
        elif segment_id == 'NM1':
            return self._parse_nm1_segment(segment)
        
        return None
    
    def _parse_clm_segment(self, segment: Any) -> Dict[str, Any]:
        """Parse CLM (Claim) segment."""
        elements = getattr(segment, 'elements', [])
        return {
            'segment_type': 'CLM',
            'claim_number': elements[0] if len(elements) > 0 else None,
            'claim_amount': elements[1] if len(elements) > 1 else None,
            'segment_data': elements
        }
    
    def _parse_nm1_segment(self, segment: Any) -> Dict[str, Any]:
        """Parse NM1 (Name) segment."""
        elements = getattr(segment, 'elements', [])
        return {
            'segment_type': 'NM1',
            'entity_code': elements[0] if len(elements) > 0 else None,
            'entity_type': elements[1] if len(elements) > 1 else None,
            'last_name': elements[2] if len(elements) > 2 else None,
            'first_name': elements[3] if len(elements) > 3 else None,
            'segment_data': elements
        }
