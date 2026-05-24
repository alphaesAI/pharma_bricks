from pyedi import SchemaMapper
from .mappings.edi_mapping import MAPPING_DEFINITION

class ETLSchemaMapper:
    """Production-grade schema mapper utilizing structural dependency injection."""

    def __init__(self, mapping_definition: dict = MAPPING_DEFINITION):
        if not mapping_definition:
            raise ValueError("Mapping definition dictionary cannot be empty or None.")
        self.mapper = SchemaMapper(mapping_definition)

    def map(self, structured_json: dict) -> dict:
        if not structured_json:
            return {}
        return self.mapper.map(structured_json)