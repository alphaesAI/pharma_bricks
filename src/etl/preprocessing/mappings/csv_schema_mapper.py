# pyrefly: ignore [missing-import]
from pyedi import SchemaMapper
from ..mapper import ETLSchemaMapper  # FIX 1: Point to correct file mapper.py
from .member_7_12_mapping import MEMBER_7_12_MAPPING_DEFINITION
from .submitted837professionaloutboundclaims_mapping import SUBMITTED837PROFESSIONALOUTBOUNDCLAIMS_MAPPING_DEFINITION


class CSVSchemaMapper(ETLSchemaMapper):

    def __init__(self):
        # FIX 2: Initialize parent with one of the definitions so it doesn't break,
        # or use it as the base claims mapper instance directly to optimize resources.
        super().__init__(mapping_definition=SUBMITTED837PROFESSIONALOUTBOUNDCLAIMS_MAPPING_DEFINITION)
        
        # Dedicated mapper for member processing loops
        self.member_mapper = SchemaMapper(MEMBER_7_12_MAPPING_DEFINITION)
        
        # The parent's self.mapper now houses the claims definition natively,
        # but assigning an explicit alias makes your mapping code downstream obvious.
        self.claims_mapper = self.mapper 

    def normalize(self, structured_json: dict, generic_json: dict) -> dict:
        """
        FIX 3: Explicit stub/implementation for structural context injection.
        Merge or normalize envelope details back into target transaction payload structure.
        """
        if not generic_json:
            return structured_json
            
        # Example processing: Inject top level interchange metadata context back down
        normalized = structured_json.copy()
        normalized["_meta_context"] = generic_json.get("interchange", {})
        return normalized

    def map_member(self, structured_json: dict, generic_json: dict = None) -> dict:
        """Map subscriber details to member CSV keys."""
        if generic_json:
            structured_json = self.normalize(structured_json, generic_json)
        return self.member_mapper.map(structured_json)

    def map_claims(self, structured_json: dict, generic_json: dict = None) -> dict:
        """Map claim loops to flat professional claim CSV keys."""
        if generic_json:
            structured_json = self.normalize(structured_json, generic_json)
        return self.claims_mapper.map(structured_json)