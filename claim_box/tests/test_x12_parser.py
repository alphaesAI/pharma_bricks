"""
Unit tests for X12 Parser module.
"""

import unittest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import json

from claim_box.preprocessing.x12_parser import X12Parser
from claim_box.preprocessing.segment_extractor import SegmentExtractor, Segment, LoopType
from claim_box.preprocessing.claim_builder import ClaimBuilder, Claim, Provider, Person, ServiceLine


class TestX12Parser(unittest.TestCase):
    """Test cases for X12Parser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = X12Parser()
    
    def test_init_without_config(self):
        """Test parser initialization without config."""
        parser = X12Parser()
        self.assertIsNone(parser.config_path)
        self.assertEqual(parser.config, {})
    
    @patch('builtins.open', unittest.mock.mock_open(read_data='{}'))
    @patch('pathlib.Path.exists')
    def test_init_with_empty_config(self, mock_exists):
        """Test parser with empty config file."""
        mock_exists.return_value = True
        parser = X12Parser(config_path=Path("dummy.json"))
        self.assertEqual(parser.config, {})
    
    @patch('builtins.open', unittest.mock.mock_open(read_data='{"key": "value"}'))
    @patch('pathlib.Path.exists')
    def test_init_with_valid_config(self, mock_exists):
        """Test parser with valid config file."""
        mock_exists.return_value = True
        parser = X12Parser(config_path=Path("dummy.json"))
        self.assertEqual(parser.config, {"key": "value"})
    
    def test_parse_nonexistent_file(self):
        """Test parsing non-existent file raises exception."""
        with self.assertRaises(FileNotFoundError):
            self.parser.parse(Path("/nonexistent/file.txt"))


class TestSegmentExtractor(unittest.TestCase):
    """Test cases for SegmentExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = SegmentExtractor()
    
    def test_init(self):
        """Test extractor initialization."""
        self.assertEqual(self.extractor.current_loop, LoopType.ISA)
        self.assertEqual(self.extractor.hl_stack, [])
    
    def test_create_segment_with_none(self):
        """Test creating segment from None data."""
        result = self.extractor._create_segment(None)
        self.assertIsNone(result)
    
    def test_determine_loop_type_isa(self):
        """Test determining ISA loop type."""
        result = self.extractor._determine_loop_type('ISA', [])
        self.assertEqual(result, LoopType.ISA)
    
    def test_determine_loop_type_gs(self):
        """Test determining GS loop type."""
        result = self.extractor._determine_loop_type('GS', [])
        self.assertEqual(result, LoopType.GS)
    
    def test_determine_loop_type_st(self):
        """Test determining ST loop type."""
        result = self.extractor._determine_loop_type('ST', [])
        self.assertEqual(result, LoopType.ST)
    
    def test_determine_loop_type_clm(self):
        """Test determining CLM loop type."""
        result = self.extractor._determine_loop_type('CLM', [])
        self.assertEqual(result, LoopType.CLAIM_2300)
    
    def test_determine_nm1_loop_submitter(self):
        """Test determining NM1 loop for submitter."""
        result = self.extractor._determine_nm1_loop(['41', '1', 'SMITH'])
        self.assertEqual(result, LoopType.HEADER_1000A)
    
    def test_determine_nm1_loop_receiver(self):
        """Test determining NM1 loop for receiver."""
        result = self.extractor._determine_nm1_loop(['40', '2', 'ACME'])
        self.assertEqual(result, LoopType.HEADER_1000B)
    
    def test_determine_nm1_loop_subscriber(self):
        """Test determining NM1 loop for subscriber."""
        result = self.extractor._determine_nm1_loop(['IL', '1', 'JONES', 'JOHN'])
        self.assertEqual(result, LoopType.SUBSCRIBER_2000B)
    
    def test_determine_nm1_loop_patient(self):
        """Test determining NM1 loop for patient."""
        result = self.extractor._determine_nm1_loop(['QC', '1', 'SMITH', 'JANE'])
        self.assertEqual(result, LoopType.PATIENT_2000C)
    
    def test_get_segments_by_type(self):
        """Test getting segments by loop type."""
        segment = Segment(seg_id='ISA', elements=['00'], loop_type=LoopType.ISA)
        categorized = {LoopType.ISA: [segment]}
        
        result = self.extractor.get_segments_by_type(categorized, LoopType.ISA)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].seg_id, 'ISA')


class TestClaimBuilder(unittest.TestCase):
    """Test cases for ClaimBuilder class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.builder = ClaimBuilder()
    
    def test_init(self):
        """Test builder initialization."""
        self.assertEqual(self.builder.claims, [])
        self.assertIsNone(self.builder.current_claim)
    
    def test_parse_clm_segment(self):
        """Test parsing CLM segment."""
        segment = Segment(
            seg_id='CLM',
            elements=['12345', '500.00'],
            loop_type=LoopType.CLAIM_2300
        )
        claim = Claim()
        self.builder._parse_clm_segment(segment, claim)
        
        self.assertEqual(claim.claim_id, '12345')
        self.assertEqual(claim.claim_amount, 500.00)
    
    def test_parse_clm_segment_with_facility(self):
        """Test parsing CLM segment with facility code."""
        segment = Segment(
            seg_id='CLM',
            elements=['12345', '1000', '', '', '11:B:1'],
            loop_type=LoopType.CLAIM_2300
        )
        claim = Claim()
        self.builder._parse_clm_segment(segment, claim)
        
        self.assertEqual(claim.claim_id, '12345')
        self.assertEqual(claim.claim_amount, 1000.00)
        self.assertEqual(claim.facility_code, '11')
    
    def test_parse_nm1_segment_for_provider(self):
        """Test parsing NM1 for billing provider."""
        segments_by_loop = {
            LoopType.BILLING_PROVIDER_2000A: [
                Segment(seg_id='NM1', elements=['85', '1', 'DOE', 'JANE', '', '', '', '', '1234567890'], loop_type=LoopType.BILLING_PROVIDER_2000A)
            ]
        }
        
        provider = self.builder._parse_provider(segments_by_loop)
        
        self.assertEqual(provider.last_name, 'DOE')
        self.assertEqual(provider.first_name, 'JANE')
        self.assertEqual(provider.npi, '1234567890')
    
    def test_parse_nm1_segment_for_subscriber(self):
        """Test parsing subscriber information."""
        segments_by_loop = {
            LoopType.SUBSCRIBER_2000B: [
                Segment(seg_id='NM1', elements=['IL', '1', 'SMITH', 'JOHN', 'A', '', '', '', 'MEMBER123'], loop_type=LoopType.SUBSCRIBER_2000B),
                Segment(seg_id='DMG', elements=['D8', '19800101', 'M'], loop_type=LoopType.SUBSCRIBER_2000B)
            ]
        }
        
        subscriber = self.builder._parse_subscriber(segments_by_loop)
        
        self.assertEqual(subscriber.last_name, 'SMITH')
        self.assertEqual(subscriber.first_name, 'JOHN')
        self.assertEqual(subscriber.middle_name, 'A')
        self.assertEqual(subscriber.member_id, 'MEMBER123')
        self.assertEqual(subscriber.date_of_birth, '19800101')
        self.assertEqual(subscriber.gender, 'M')
    
    def test_parse_sv1_segment(self):
        """Test parsing SV1 service line segment."""
        segment = Segment(
            seg_id='SV1',
            elements=['99213:25:GT', '200.00', 'MJ', '1', '', '', '1:2:3:4', '', '', '', '1'],
            loop_type=LoopType.SERVICE_2400
        )
        service_line = ServiceLine()
        
        self.builder._parse_sv1_segment(segment, service_line)
        
        self.assertEqual(service_line.procedure_code, '99213')
        self.assertEqual(service_line.procedure_modifier1, '25')
        self.assertEqual(service_line.procedure_modifier2, 'GT')
        self.assertEqual(service_line.charge_amount, 200.00)
        self.assertEqual(service_line.unit_count, 1.0)
        self.assertEqual(service_line.diagnosis_code_pointer1, '1')
        self.assertEqual(service_line.diagnosis_code_pointer2, '2')
    
    def test_claims_to_dict(self):
        """Test converting claims to dictionaries."""
        claim = Claim()
        claim.claim_id = 'TEST123'
        claim.claim_amount = 100.00
        claim.provider = Provider(npi='1234567890', last_name='DOE', first_name='JOHN')
        claim.subscriber = Person(last_name='SMITH', first_name='JANE', member_id='M001')
        
        result = self.builder._claim_to_dict(claim)
        
        self.assertEqual(result['claim_id'], 'TEST123')
        self.assertEqual(result['claim_amount'], 100.00)
        self.assertEqual(result['provider']['npi'], '1234567890')
        self.assertEqual(result['subscriber']['member_id'], 'M001')
        self.assertIsNone(result['patient'])  # No patient set


if __name__ == '__main__':
    unittest.main()
