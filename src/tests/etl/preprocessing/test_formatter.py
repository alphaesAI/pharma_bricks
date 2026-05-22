import unittest
from unittest.mock import MagicMock
from src.etl.preprocessing.formatter import TransactionFormatter

class TestTransactionFormatter(unittest.TestCase):
    def test_formatter_with_mocked_parser_output(self):
        # 1. Arrange: Create a minimal mock input that mirrors your EDIParser stream output
        mock_generic_json = [
            {
                "segment_id": "NM1",
                "x12_path": "/ISA_LOOP/GS_LOOP/ST_LOOP/ST",
                "elements": {
                    "NM101": "85",
                    "NM102": "2",
                    "NM103": "METRO HEALTH CENTER",
                    "NM108": "XX",
                    "NM109": "1234567890"
                },
                "segment_name": "Transaction Set Header",
                "loop_id": "ST_LOOP",
                "hierarchical_context": {
                    "hl_id": "1",
                    "hl_parent": "",
                    "hl_level": "20",
                    "hl_level_name": "Information Source",
                    "hl_path": ["1"]
                }
            },
            {
                "segment_id": "NM1",
                "x12_path": "/ISA_LOOP/GS_LOOP/ST_LOOP/ST",
                "elements": {
                    "NM101": "IL",
                    "NM102": "1",
                    "NM103": "DOE",
                    "NM104": "JOHN",
                    "NM108": "MI",
                    "NM109": "W123456789"
                },
                "segment_name": "Transaction Set Header",
                "loop_id": "ST_LOOP",
                "hierarchical_context": {
                    "hl_id": "2",
                    "hl_parent": "1",
                    "hl_level": "22",
                    "hl_level_name": "Subscriber",
                    "hl_path": ["1", "2"]
                }
            }
        ]

        formatter = TransactionFormatter()

        # 2. Act: Pass the static mock data directly to the formatter
        structured_json = formatter.format(mock_generic_json)

        # 3. Assert: Verify the formatter mapped the flat segments to your nested structure properly
        self.assertIsNotNone(structured_json)
        
        # Check if it successfully extracted detail loop structures
        self.assertIn("detail", structured_json)
        submitter_loop = structured_json["detail"].get("submitter_NM1_loop", {})
        nm1_headers = submitter_loop.get("transaction_set_header_NM1", [])
        
        # Verify specific counts or target fields are populated based on your schema mapping rules
        self.assertTrue(len(nm1_headers) > 0)
        
        # Example validation: check if the billing provider name was mapped correctly from NM103
        billing_provider = next((x for x in nm1_headers if x.get("entity_identifier_code") == "85"), None)
        self.assertIsNotNone(billing_provider)
        self.assertEqual(billing_provider.get("billing_provider_name"), "METRO HEALTH CENTER")

if __name__ == "__main__":
    unittest.main()