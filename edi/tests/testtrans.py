from edi.pyedi.parsers.edi_parser import EDIParser
from edi.pyedi.formatters.transaction_formatters import TransactionFormatter
from edi.pyedi.mappers.mappings.schema_mapper import ETLSchemaMapper
from edi.pyedi.tables.subscriber.subscriber import SubscriberProcessor
from edi.pyedi.tables.interchange.interchange import InterchangeProcessor
from edi.pyedi.tables.functional_group.functional_group import FunctionalGroupProcessor
from edi.pyedi.tables.transaction_header.transaction_header import TransactionHeaderProcessor
from edi.pyedi.tables.submitter.submitter import SubmitterProcessor
from edi.pyedi.tables.receiver.receiver import ReceiverProcessor
from edi.pyedi.tables.billing_provider.billing_provider import BillingProviderProcessor
from edi.pyedi.tables.rendering_provider.rendering_provider import RenderingProviderProcessor
from edi.pyedi.tables.payer.payer import PayerProcessor
from edi.pyedi.tables.claim.claim import ClaimProcessor
from edi.pyedi.tables.claim_dates.claim_dates import ClaimDatesProcessor
from edi.pyedi.tables.diagnosis.diagnosis import DiagnosisProcessor
from edi.pyedi.tables.service_line.service_line import ServiceLineProcessor
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
    database="edi_pipeline",
    user="postgres",
    password="12345"
)

InterchangeProcessor(conn).process(result)
FunctionalGroupProcessor(conn).process(result)
TransactionHeaderProcessor(conn).process(result)
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

conn.close()


