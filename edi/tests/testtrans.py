from edi.pyedi.parsers.edi_parser import EDIParser
from edi.pyedi.formatters.transaction_formatters import TransactionFormatter
from edi.pyedi.mappers.mappings.schema_mapper import ETLSchemaMapper

parser = EDIParser()
formatter = TransactionFormatter()
schema_mapper = ETLSchemaMapper()

result = parser.parse("samples/837_actual_data.txt")
result = formatter.format(result)
result = schema_mapper.map(result)

print(result)