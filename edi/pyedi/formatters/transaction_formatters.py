from pyedi import StructuredFormatter


class TransactionFormatter:

    def __init__(self):
        self.formatter = StructuredFormatter()

    def format(self, generic_json: dict):

        structured_json = self.formatter.format(
            generic_json,
            include_technical=True
        )

        return structured_json

if __name__ == "__main__":
    formatter = TransactionFormatter()
    result = formatter.format({"test": "test"})
    print(result)
