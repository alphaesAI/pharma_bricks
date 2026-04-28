"""Claim Builder - Simplified version."""

import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict

from .segment_extractor import Segment, LoopType

logger = logging.getLogger(__name__)


@dataclass
class Provider:
    npi: Optional[str] = None
    organization_name: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


@dataclass
class Person:
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    member_id: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None


@dataclass
class ServiceLine:
    line_number: Optional[int] = None
    service_date: Optional[str] = None
    procedure_code: Optional[str] = None
    charge_amount: Optional[float] = None
    unit_count: Optional[float] = None


@dataclass
class Claim:
    claim_id: Optional[str] = None
    claim_amount: Optional[float] = None
    facility_code: Optional[str] = None
    
    provider: Provider = field(default_factory=Provider)
    subscriber: Person = field(default_factory=Person)
    patient: Optional[Person] = None
    service_lines: List[ServiceLine] = field(default_factory=list)
    diagnosis_codes: List[str] = field(default_factory=list)


class ClaimBuilder:
    """Builds Claim objects from categorized X12 segments."""
    
    def build_claims(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> List[Claim]:
        """Build Claim objects from categorized segments."""
        claims = []
        claim_segments = segments_by_loop.get(LoopType.CLAIM_2300, [])
        
        for clm_seg in claim_segments:
            claim = self._build_single_claim(clm_seg, segments_by_loop)
            if claim:
                claims.append(claim)
        
        logger.info(f"Built {len(claims)} claims")
        return claims
    
    def _build_single_claim(self, clm_segment: Segment, segments_by_loop: Dict[LoopType, List[Segment]]) -> Optional[Claim]:
        """Build a single claim."""
        try:
            claim = Claim()
            
            # Parse CLM segment
            claim.claim_id = clm_segment.get_element(1)
            amount_str = clm_segment.get_element(2)
            if amount_str:
                try:
                    claim.claim_amount = float(amount_str)
                except ValueError:
                    pass
            
            facility_info = clm_segment.get_element(5)
            if facility_info:
                claim.facility_code = facility_info.split(':')[0]
            
            # Parse provider, subscriber, patient
            claim.provider = self._parse_provider(segments_by_loop)
            claim.subscriber = self._parse_subscriber(segments_by_loop)
            
            patient_segments = segments_by_loop.get(LoopType.PATIENT_2000C, [])
            if patient_segments:
                claim.patient = self._parse_patient(patient_segments)
            
            # Service lines and diagnosis
            claim.service_lines = self._parse_service_lines(segments_by_loop)
            claim.diagnosis_codes = self._parse_diagnosis_codes(segments_by_loop)
            
            return claim
            
        except Exception as e:
            logger.warning(f"Failed to build claim: {e}")
            return None
    
    def _parse_provider(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> Provider:
        """Parse billing provider from 2000A loop."""
        provider = Provider()
        
        for seg in segments_by_loop.get(LoopType.BILLING_PROVIDER_2000A, []):
            if seg.seg_id == 'NM1' and seg.get_element(1) == '85':
                provider.npi = seg.get_element(9)
                if seg.get_element(2) == '2':  # Organization
                    provider.organization_name = seg.get_element(3)
                else:
                    provider.last_name = seg.get_element(3)
                    provider.first_name = seg.get_element(4)
                break
        
        return provider
    
    def _parse_subscriber(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> Person:
        """Parse subscriber from 2000B loop."""
        subscriber = Person()
        
        for seg in segments_by_loop.get(LoopType.SUBSCRIBER_2000B, []):
            if seg.seg_id == 'NM1' and seg.get_element(1) == 'IL':
                subscriber.last_name = seg.get_element(3)
                subscriber.first_name = seg.get_element(4)
                subscriber.member_id = seg.get_element(9)
            elif seg.seg_id == 'DMG':
                subscriber.date_of_birth = seg.get_element(2)
                subscriber.gender = seg.get_element(3)
        
        return subscriber
    
    def _parse_patient(self, patient_segments: List[Segment]) -> Person:
        """Parse patient from 2000C loop."""
        patient = Person()
        
        for seg in patient_segments:
            if seg.seg_id == 'NM1' and seg.get_element(1) == 'QC':
                patient.last_name = seg.get_element(3)
                patient.first_name = seg.get_element(4)
            elif seg.seg_id == 'DMG':
                patient.date_of_birth = seg.get_element(2)
                patient.gender = seg.get_element(3)
        
        return patient
    
    def _parse_service_lines(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> List[ServiceLine]:
        """Parse service lines from 2400 loop."""
        service_lines: List[ServiceLine] = []
        
        for seg in segments_by_loop.get(LoopType.SERVICE_2400, []):
            if seg.seg_id == 'LX':
                line = ServiceLine()
                line_num = seg.get_element(1)
                if line_num:
                    line.line_number = int(line_num)
                service_lines.append(line)
                
            elif seg.seg_id == 'SV1' and service_lines:
                line = service_lines[-1]
                proc_info = seg.get_element(1)
                if proc_info:
                    line.procedure_code = proc_info.split(':')[0]
                charge = seg.get_element(2)
                if charge:
                    try:
                        line.charge_amount = float(charge)
                    except ValueError:
                        pass
                        
            elif seg.seg_id == 'DTP' and service_lines:
                line = service_lines[-1]
                if seg.get_element(1) == '472':
                    line.service_date = seg.get_element(3)
        
        return service_lines
    
    def _parse_diagnosis_codes(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> List[str]:
        """Parse diagnosis codes from HI segments."""
        codes = []
        
        for seg in segments_by_loop.get(LoopType.CLAIM_2300, []):
            if seg.seg_id == 'HI':
                for i in range(1, 13):
                    diag = seg.get_element(i)
                    if diag:
                        parts = diag.split(':')
                        if len(parts) > 1:
                            codes.append(parts[1])
        
        return codes
    
    def claims_to_dict(self, claims: List[Claim]) -> List[dict]:
        """Convert claims to dictionaries using dataclass asdict."""
        return [asdict(c) for c in claims]
