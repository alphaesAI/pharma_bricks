# pyrefly: ignore [missing-import]
from pyedi import SchemaMapper
from .mapping import MAPPING_DEFINITION


class ETLSchemaMapper:

    def __init__(self):
        self.mapper = SchemaMapper(MAPPING_DEFINITION)
        print("mapping object: ", self.mapper)
        print("mapping definition: ", MAPPING_DEFINITION)

    def map(self, structured_json: dict):

        transformed_json = self.mapper.map(structured_json)

        return transformed_json