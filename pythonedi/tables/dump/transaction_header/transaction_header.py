from psycopg2.extras import RealDictCursor


class TransactionHeaderProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "transaction_header" not in mapped_data:
            print("transaction_header not found")
            return

        transaction_header = mapped_data["transaction_header"]
        self.insert(transaction_header)

    def insert(self, transaction_header: dict):

        columns = list(transaction_header.keys())
        print("Columns:", columns)

        values = list(transaction_header.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO transaction_header (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        """

        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

        print("transaction_header inserted successfully")
