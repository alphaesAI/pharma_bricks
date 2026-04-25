"""
Segment Extractor Module

Extracts and categorizes X12 segments by loop type.
Follows Single Responsibility Principle - only handles segment extraction.
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class LoopType(Enum):
    """X12 837 Loop Types."""
    ISA = "ISA"  # Interchange Control Header
    GS = "GS"    # Functional Group Header
    ST = "ST"    # Transaction Set Header
    HEADER_1000A = "1000A"  # Submitter
    HEADER_1000B = "1000B"  # Receiver
    BILLING_PROVIDER_2000A = "2000A"  # Billing Provider HL
    SUBSCRIBER_2000B = "2000B"  # Subscriber HL
    PATIENT_2000C = "2000C"  # Patient HL
    CLAIM_2300 = "2300"  # Claim Information
    SERVICE_2400 = "2400"  # Service Line
    TRAILER = "TRAILER"  # SE/GE/IEA


@dataclass
class Segment:
    """Represents a single X12 segment."""
    seg_id: str
    elements: List[str]
    loop_type: LoopType
    raw_segment: str = ""
    
    def get_element(self, index: int) -> Optional[str]:
        """Get element at index (1-based, returns None if not exists)."""
        if 1 <= index <= len(self.elements):
            return self.elements[index - 1]
        return None


class SegmentExtractor:
    """
    Extracts and categorizes X12 segments.
    
    Responsibilities:
    - Identify segment types
    - Track loop hierarchy (HL segments)
    - Group segments by loop type
    """
    
    def __init__(self):
        self.current_loop = LoopType.ISA
        self.hl_stack: List[str] = []
        logger.info("SegmentExtractor initialized")
    
    def extract_segments(self, segments_data: List[Any]) -> Dict[LoopType, List[Segment]]:
        """
        Extract and categorize segments by loop type.
        
        Args:
            segments_data: List of raw segment data from X12 parser
            
        Returns:
            Dictionary mapping LoopType to list of Segment objects
        """
        categorized: Dict[LoopType, List[Segment]] = {
            loop: [] for loop in LoopType
        }
        
        try:
            for raw_seg in segments_data:
                segment = self._create_segment(raw_seg)
                if segment:
                    categorized[segment.loop_type].append(segment)
                    
        except Exception as e:
            logger.error(f"Error extracting segments: {e}")
            raise
        
        return categorized
    
    def _create_segment(self, raw_seg: Any) -> Optional[Segment]:
        """Create Segment object from raw data."""
        try:
            seg_id = getattr(raw_seg, 'seg_id', None)
            if not seg_id:
                return None
            
            elements = getattr(raw_seg, 'elements', [])
            raw_text = getattr(raw_seg, 'format', lambda: "")()
            
            # Determine loop type
            loop_type = self._determine_loop_type(seg_id, elements)
            
            # Update loop tracking
            if seg_id == 'HL':
                self._update_hl_stack(elements)
            
            return Segment(
                seg_id=seg_id,
                elements=elements,
                loop_type=loop_type,
                raw_segment=raw_text
            )
            
        except Exception as e:
            logger.warning(f"Failed to create segment: {e}")
            return None
    
    def _determine_loop_type(self, seg_id: str, elements: List[str]) -> LoopType:
        """Determine loop type based on segment ID and context."""
        
        if seg_id == 'ISA':
            return LoopType.ISA
        elif seg_id == 'GS':
            return LoopType.GS
        elif seg_id == 'ST':
            return LoopType.ST
        elif seg_id == 'SE':
            return LoopType.TRAILER
        elif seg_id == 'GE':
            return LoopType.TRAILER
        elif seg_id == 'IEA':
            return LoopType.TRAILER
        elif seg_id == 'NM1':
            # NM1 appears in multiple loops - determine by context
            return self._determine_nm1_loop(elements)
        elif seg_id == 'CLM':
            return LoopType.CLAIM_2300
        elif seg_id in ['LX', 'SV1', 'DTP']:
            return LoopType.SERVICE_2400
        elif seg_id in ['HL']:
            return self._determine_hl_loop(elements)
        
        # Default to current loop
        return self.current_loop
    
    def _determine_nm1_loop(self, elements: List[str]) -> LoopType:
        """Determine NM1 loop type based on qualifier."""
        if len(elements) < 1:
            return self.current_loop
        
        qualifier = elements[0]
        
        # NM1 qualifiers: 41=Submitter, 40=Receiver, IL=Insured/Subscriber, QC=Patient
        if qualifier == '41':
            return LoopType.HEADER_1000A
        elif qualifier == '40':
            return LoopType.HEADER_1000B
        elif qualifier == 'IL':
            return LoopType.SUBSCRIBER_2000B
        elif qualifier == 'QC':
            return LoopType.PATIENT_2000C
        
        return self.current_loop
    
    def _determine_hl_loop(self, elements: List[str]) -> LoopType:
        """Determine HL (Hierarchical Level) loop type."""
        if len(elements) < 3:
            return self.current_loop
        
        # HL03 = hierarchical level code
        # 20=Information Source (Billing Provider)
        # 21=Information Receiver (Subscriber)
        # 22=Subscriber
        # 23=Dependent (Patient)
        level_code = elements[2] if len(elements) > 2 else ""
        
        if level_code == '20':
            self.current_loop = LoopType.BILLING_PROVIDER_2000A
            return LoopType.BILLING_PROVIDER_2000A
        elif level_code == '21':
            self.current_loop = LoopType.SUBSCRIBER_2000B
            return LoopType.SUBSCRIBER_2000B
        elif level_code == '22':
            self.current_loop = LoopType.SUBSCRIBER_2000B
            return LoopType.SUBSCRIBER_2000B
        elif level_code == '23':
            self.current_loop = LoopType.PATIENT_2000C
            return LoopType.PATIENT_2000C
        
        return self.current_loop
    
    def _update_hl_stack(self, elements: List[str]) -> None:
        """Update HL tracking stack."""
        if len(elements) > 0:
            hl_id = elements[0]
            self.hl_stack.append(hl_id)
    
    def get_segments_by_type(self, 
                            categorized: Dict[LoopType, List[Segment]], 
                            loop_type: LoopType) -> List[Segment]:
        """Get all segments of a specific loop type."""
        return categorized.get(loop_type, [])
