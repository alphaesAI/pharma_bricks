# pyrefly: ignore [missing-import]
from pyedi import SchemaMapper
from .schema_mapper import ETLSchemaMapper
from .member_7_12_mapping import MEMBER_7_12_MAPPING_DEFINITION
from .submitted837professionaloutboundclaims_mapping import SUBMITTED837PROFESSIONALOUTBOUNDCLAIMS_MAPPING_DEFINITION


class CSVSchemaMapper(ETLSchemaMapper):

    def __init__(self):
        super().__init__()
        self.member_mapper = SchemaMapper(MEMBER_7_12_MAPPING_DEFINITION)
        self.claims_mapper = SchemaMapper(SUBMITTED837PROFESSIONALOUTBOUNDCLAIMS_MAPPING_DEFINITION)

    def map_member(self, structured_json: dict, generic_json: dict = None) -> dict:
        """
        Map subscriber details to member CSV keys
        """
        if generic_json:
            structured_json = self.normalize(structured_json, generic_json)
        return self.member_mapper.map(structured_json)

    def map_claims(self, structured_json: dict, generic_json: dict = None) -> dict:
        """
        Map claim loops to flat professional claim CSV keys
        """
        if generic_json:
            structured_json = self.normalize(structured_json, generic_json)
        return self.claims_mapper.map(structured_json)

