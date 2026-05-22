from src.etl.preprocessing.formatter import TransactionFormatter
from src.etl.preprocessing.parser import EDIParser

def test_formatter():
    formatter = TransactionFormatter()
    generic_json = EDIParser().parse("samples/837_actual_data.txt")
    structured_json = formatter.format(generic_json)
    # print("\n\n\nstructured json: ", structured_json)
