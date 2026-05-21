from .parsers.edi_parser import EDIParser
from .formatters.transaction_formatters import TransactionFormatter
from .mappers.mappings.schema_mapper import ETLSchemaMapper
from .mappers.mappings.csv_schema_mapper import CSVSchemaMapper
from .consolidation.csvconverter import CSVConverter
from .tables.processors import *

import psycopg2

parser = EDIParser()
formatter = TransactionFormatter()
schema_mapper = ETLSchemaMapper()

generic_json = parser.parse("samples/dummy_data.txt")
print("Parsed result:", generic_json)
structured_json = formatter.format(generic_json)
print("\n\n\n\nFormatted result:", structured_json)
result = schema_mapper.map(structured_json, generic_json=generic_json)
print("\n\n\n\nMapped result:", result)

conn = psycopg2.connect(
    host="localhost",
    database="edi",
    user="postgres",
    password="12345"
)

InterchangeProcessor(conn).process(result)
FunctionalGroupProcessor(conn).process(result)
# TransactionHeaderProcessor(conn).process(result)
SubmitterProcessor(conn).process(result)
ReceiverProcessor(conn).process(result)
BillingProviderProcessor(conn).process(result)
RenderingProviderProcessor(conn).process(result)
SubscriberProcessor(conn).process(result)
PayerProcessor(conn).process(result)
ClaimProcessor(conn).process(result)
ClaimDatesProcessor(conn).process(result)
DiagnosisProcessor(conn).process(result)
ServiceLineProcessor(conn).process(result)

# -----------------------------------
# Consolidation Layer (CSV Export)
# -----------------------------------
print("\n--- Starting CSV Export Pipeline ---")
csv_mapper = CSVSchemaMapper()
member_mapped = csv_mapper.map_member(structured_json, generic_json=generic_json)
claims_mapped = csv_mapper.map_claims(structured_json, generic_json=generic_json)

converter = CSVConverter(schemas_dir="bis-datalake-dev/JSON/Schema")
converter.convert_members(member_mapped, "output/member_7.12.csv")
converter.convert_claims(claims_mapped, "output/claims_7.12.csv")
print("--- CSV Export Pipeline Completed Successfully ---\n")

# MedicalClaimHeaderProcessor(conn).process(result)

conn.commit()

conn.close()