"""
Claim Builder Module

Builds structured claim objects from extracted X12 segments.
Follows Builder Pattern for constructing complex claim objects.
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime

from .segment_extractor import Segment, LoopType

logger = logging.getLogger(__name__)


@dataclass
class Provider:
    """Billing Provider entity."""
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
    """Subscriber or Patient entity."""
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    member_id: Optional[str] = None
    ssn: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


@dataclass
class ServiceLine:
    """Individual service line item."""
    line_number: Optional[int] = None
    service_date: Optional[str] = None
    procedure_code: Optional[str] = None
    procedure_modifier1: Optional[str] = None
    procedure_modifier2: Optional[str] = None
    procedure_modifier3: Optional[str] = None
    procedure_modifier4: Optional[str] = None
    diagnosis_code_pointer1: Optional[str] = None
    diagnosis_code_pointer2: Optional[str] = None
    diagnosis_code_pointer3: Optional[str] = None
    diagnosis_code_pointer4: Optional[str] = None
    charge_amount: Optional[float] = None
    unit_count: Optional[float] = None


@dataclass
class Claim:
    """Complete claim entity."""
    claim_id: Optional[str] = None
    claim_amount: Optional[float] = None
    facility_code: Optional[str] = None
    claim_frequency: Optional[str] = None
    provider_signature: Optional[str] = None
    assignment_ind: Optional[str] = None
    benefit_assignment: Optional[str] = None
    release_info: Optional[str] = None
    patient_signature: Optional[str] = None
    
    provider: Provider = field(default_factory=Provider)
    subscriber: Person = field(default_factory=Person)
    patient: Optional[Person] = None
    service_lines: List[ServiceLine] = field(default_factory=list)
    diagnosis_codes: List[str] = field(default_factory=list)
    
    admission_date: Optional[str] = None
    discharge_date: Optional[str] = None
    statement_from_date: Optional[str] = None
    statement_to_date: Optional[str] = None


class ClaimBuilder:
    """
    Builds Claim objects from categorized X12 segments.
    
    Responsibilities:
    - Aggregate segments into complete claims
    - Map segment elements to claim fields
    - Handle dependent (patient) vs subscriber claims
    """
    
    def __init__(self):
        self.claims: List[Claim] = []
        self.current_claim: Optional[Claim] = None
        logger.info("ClaimBuilder initialized")
    
    def build_claims(self, 
                     segments_by_loop: Dict[LoopType, List[Segment]]) -> List[Claim]:
        """
        Build complete Claim objects from categorized segments.
        
        Args:
            segments_by_loop: Dictionary of segments by loop type
            
        Returns:
            List of complete Claim objects
        """
        try:
            self.claims = []
            
            # Get all CLM (claim) segments
            claim_segments = segments_by_loop.get(LoopType.CLAIM_2300, [])
            
            for clm_seg in claim_segments:
                claim = self._build_single_claim(clm_seg, segments_by_loop)
                if claim:
                    self.claims.append(claim)
            
            logger.info(f"Built {len(self.claims)} complete claims")
            return self.claims
            
        except Exception as e:
            logger.error(f"Error building claims: {e}")
            raise
    
    def _build_single_claim(self, 
                           clm_segment: Segment,
                           segments_by_loop: Dict[LoopType, List[Segment]]) -> Optional[Claim]:
        """Build a single claim from CLM segment and related data."""
        try:
            claim = Claim()
            
            # Parse CLM segment
            self._parse_clm_segment(clm_segment, claim)
            
            # Find and parse provider
            claim.provider = self._parse_provider(segments_by_loop)
            
            # Find and parse subscriber
            claim.subscriber = self._parse_subscriber(segments_by_loop)
            
            # Find and parse patient (if exists - indicates dependent claim)
            patient_segments = segments_by_loop.get(LoopType.PATIENT_2000C, [])
            if patient_segments:
                claim.patient = self._parse_patient(patient_segments)
            
            # Parse service lines
            claim.service_lines = self._parse_service_lines(segments_by_loop)
            
            # Parse diagnosis codes from HI segments
            claim.diagnosis_codes = self._parse_diagnosis_codes(segments_by_loop)
            
            return claim
            
        except Exception as e:
            logger.warning(f"Failed to build claim from segment: {e}")
            return None
    
    def _parse_clm_segment(self, segment: Segment, claim: Claim) -> None:
        """Parse CLM (Claim Information) segment."""
        # CLM*claim_id*amount*...*facility_code:...*frequency*...
        claim.claim_id = segment.get_element(1)
        
        try:
            amount_str = segment.get_element(2)
            if amount_str:
                claim.claim_amount = float(amount_str)
        except ValueError:
            claim.claim_amount = None
        
        # Element 5 contains facility code and other qualifiers
        facility_info = segment.get_element(5)
        if facility_info:
            parts = facility_info.split(':')
            if len(parts) > 0:
                claim.facility_code = parts[0]
        
        claim.claim_frequency = segment.get_element(6)
        
        # Assignment and signature indicators (elements 7-10)
        claim.provider_signature = segment.get_element(7)
        claim.assignment_ind = segment.get_element(8)
        claim.benefit_assignment = segment.get_element(9)
        claim.release_info = segment.get_element(10)
        claim.patient_signature = segment.get_element(11)
    
    def _parse_provider(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> Provider:
        """Parse billing provider from NM1 segments."""
        provider = Provider()
        
        # Find NM1*85 (Billing Provider) in 2000A loop
        nm1_segments = segments_by_loop.get(LoopType.BILLING_PROVIDER_2000A, [])
        
        for seg in nm1_segments:
            if seg.seg_id == 'NM1' and seg.get_element(1) == '85':
                # NM1*85*entity_type*last*first*...*npi
                provider.last_name = seg.get_element(3)
                provider.first_name = seg.get_element(4)
                provider.npi = seg.get_element(9)
                
                # If entity type is 2 (non-person), name is in element 3
                entity_type = seg.get_element(2)
                if entity_type == '2':
                    provider.organization_name = seg.get_element(3)
                    provider.last_name = None
                
                break
        
        return provider
    
    def _parse_subscriber(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> Person:
        """Parse subscriber (insured person) information."""
        subscriber = Person()
        
        # Find NM1*IL (Insured/Subscriber) in 2000B loop
        nm1_segments = segments_by_loop.get(LoopType.SUBSCRIBER_2000B, [])
        
        for seg in nm1_segments:
            if seg.seg_id == 'NM1' and seg.get_element(1) == 'IL':
                subscriber.last_name = seg.get_element(3)
                subscriber.first_name = seg.get_element(4)
                subscriber.middle_name = seg.get_element(5)
                subscriber.member_id = seg.get_element(9)
                break
        
        # Get additional subscriber info from other segments
        subscriber_segments = segments_by_loop.get(LoopType.SUBSCRIBER_2000B, [])
        for seg in subscriber_segments:
            if seg.seg_id == 'DMG':  # Demographics
                subscriber.date_of_birth = seg.get_element(2)
                subscriber.gender = seg.get_element(3)
        
        return subscriber
    
    def _parse_patient(self, patient_segments: List[Segment]) -> Person:
        """Parse patient (dependent) information."""
        patient = Person()
        
        for seg in patient_segments:
            if seg.seg_id == 'NM1' and seg.get_element(1) == 'QC':
                patient.last_name = seg.get_element(3)
                patient.first_name = seg.get_element(4)
                patient.middle_name = seg.get_element(5)
                
            elif seg.seg_id == 'DMG':  # Demographics
                patient.date_of_birth = seg.get_element(2)
                patient.gender = seg.get_element(3)
        
        return patient
    
    def _parse_service_lines(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> List[ServiceLine]:
        """Parse service line items from 2400 loop."""
        service_lines = []
        
        lx_segments = segments_by_loop.get(LoopType.SERVICE_2400, [])
        
        for seg in lx_segments:
            if seg.seg_id == 'LX':  # Line number
                sv_line = ServiceLine()
                sv_line.line_number = int(seg.get_element(1)) if seg.get_element(1) else None
                service_lines.append(sv_line)
                
            elif seg.seg_id == 'SV1':  # Professional service
                if service_lines:
                    current_line = service_lines[-1]
                    self._parse_sv1_segment(seg, current_line)
                    
            elif seg.seg_id == 'DTP':  # Service date
                if service_lines:
                    current_line = service_lines[-1]
                    qualifier = seg.get_element(1)
                    if qualifier == '472':  # Service date
                        current_line.service_date = seg.get_element(3)
        
        return service_lines
    
    def _parse_sv1_segment(self, segment: Segment, service_line: ServiceLine) -> None:
        """Parse SV1 (Professional Service) segment."""
        # SV1*procedure_code:mod1:mod2:mod3:mod4*charge*...*unit_count
        procedure_info = segment.get_element(1)
        if procedure_info:
            parts = procedure_info.split(':')
            if len(parts) > 0:
                service_line.procedure_code = parts[0]
            if len(parts) > 1:
                service_line.procedure_modifier1 = parts[1]
            if len(parts) > 2:
                service_line.procedure_modifier2 = parts[2]
            if len(parts) > 3:
                service_line.procedure_modifier3 = parts[3]
            if len(parts) > 4:
                service_line.procedure_modifier4 = parts[4]
        
        try:
            charge_str = segment.get_element(2)
            if charge_str:
                service_line.charge_amount = float(charge_str)
        except ValueError:
            service_line.charge_amount = None
        
        # Diagnosis code pointers (elements 7-10)
        service_line.diagnosis_code_pointer1 = segment.get_element(7)
        service_line.diagnosis_code_pointer2 = segment.get_element(8)
        service_line.diagnosis_code_pointer3 = segment.get_element(9)
        service_line.diagnosis_code_pointer4 = segment.get_element(10)
        
        try:
            unit_str = segment.get_element(11)
            if unit_str:
                service_line.unit_count = float(unit_str)
        except ValueError:
            service_line.unit_count = None
    
    def _parse_diagnosis_codes(self, segments_by_loop: Dict[LoopType, List[Segment]]) -> List[str]:
        """Parse diagnosis codes from HI segments in 2300 loop."""
        diagnosis_codes = []
        
        # HI segments contain diagnosis codes
        claim_segments = segments_by_loop.get(LoopType.CLAIM_2300, [])
        
        for seg in claim_segments:
            if seg.seg_id == 'HI':
                # HI*BK:diagnosis_code1*BF:diagnosis_code2...
                for i in range(1, 13):  # HI can have up to 12 diagnosis codes
                    diag_info = seg.get_element(i)
                    if diag_info:
                        parts = diag_info.split(':')
                        if len(parts) > 1:
                            diagnosis_codes.append(parts[1])
        
        return diagnosis_codes
    
    def claims_to_dict(self, claims: List[Claim]) -> List[Dict[str, Any]]:
        """Convert list of Claim objects to dictionaries."""
        return [self._claim_to_dict(c) for c in claims]
    
    def _claim_to_dict(self, claim: Claim) -> Dict[str, Any]:
        """Convert single Claim to dictionary."""
        return {
            'claim_id': claim.claim_id,
            'claim_amount': claim.claim_amount,
            'facility_code': claim.facility_code,
            'claim_frequency': claim.claim_frequency,
            'provider': {
                'npi': claim.provider.npi,
                'organization_name': claim.provider.organization_name,
                'last_name': claim.provider.last_name,
                'first_name': claim.provider.first_name,
            },
            'subscriber': {
                'last_name': claim.subscriber.last_name,
                'first_name': claim.subscriber.first_name,
                'member_id': claim.subscriber.member_id,
                'date_of_birth': claim.subscriber.date_of_birth,
                'gender': claim.subscriber.gender,
            },
            'patient': {
                'last_name': claim.patient.last_name,
                'first_name': claim.patient.first_name,
                'date_of_birth': claim.patient.date_of_birth,
                'gender': claim.patient.gender,
            } if claim.patient else None,
            'service_lines': [
                {
                    'line_number': sl.line_number,
                    'service_date': sl.service_date,
                    'procedure_code': sl.procedure_code,
                    'procedure_modifiers': [
                        sl.procedure_modifier1,
                        sl.procedure_modifier2,
                        sl.procedure_modifier3,
                        sl.procedure_modifier4,
                    ],
                    'charge_amount': sl.charge_amount,
                    'unit_count': sl.unit_count,
                    'diagnosis_pointers': [
                        sl.diagnosis_code_pointer1,
                        sl.diagnosis_code_pointer2,
                        sl.diagnosis_code_pointer3,
                        sl.diagnosis_code_pointer4,
                    ],
                } for sl in claim.service_lines
            ],
            'diagnosis_codes': claim.diagnosis_codes,
        }
