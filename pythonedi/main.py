from .parsers.edi_parser import EDIParser
from .formatters.transaction_formatters import TransactionFormatter
from .mappers.mappings.schema_mapper import ETLSchemaMapper
from .tables.processors import *
# from .consolidation import MedicalClaimHeaderProcessor
# from .tables.subscriber.subscriber import SubscriberProcessor
# from .tables.interchange.interchange import InterchangeProcessor
# from .tables.functional_group.functional_group import FunctionalGroupProcessor
# from .tables.transaction_header.transaction_header import TransactionHeaderProcessor
# from .tables.submitter.submitter import SubmitterProcessor
# from .tables.receiver.receiver import ReceiverProcessor
# from .tables.billing_provider.billing_provider import BillingProviderProcessor
# from .tables.rendering_provider.rendering_provider import RenderingProviderProcessor
# from .tables.payer.payer import PayerProcessor
# from .tables.claim.claim import ClaimProcessor
# from .tables.claim_dates.claim_dates import ClaimDatesProcessor
# from .tables.diagnosis.diagnosis import DiagnosisProcessor
# from .tables.service_line.service_line import ServiceLineProcessor
import psycopg2

parser = EDIParser()
formatter = TransactionFormatter()
schema_mapper = ETLSchemaMapper()

result = parser.parse("samples/837_actual_data.txt")
# print("Parsed result:", result)
result = formatter.format(result)
# print("Formatted result:", result)
result = schema_mapper.map(result)
print("Mapped result:", result)

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
ClaimDatesProcessor(conn).process(result)
DiagnosisProcessor(conn).process(result)
ServiceLineProcessor(conn).process(result)
ClaimProcessor(conn).process(result)

# -----------------------------------
# Consolidation Layer
# -----------------------------------
# MedicalClaimHeaderProcessor(conn).process(result)

conn.commit()

conn.close()