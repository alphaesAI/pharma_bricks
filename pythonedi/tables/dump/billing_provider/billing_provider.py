from psycopg2.extras import RealDictCursor


class BillingProviderProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "billing_provider" not in mapped_data:
            print("billing_provider not found")
            return

        billing_provider = mapped_data["billing_provider"]
        self.insert(billing_provider)

    def insert(self, billing_provider: dict):

        columns = list(billing_provider.keys())
        print("Columns:", columns)

        values = list(billing_provider.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO billing_provider (
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

        print("billing_provider inserted successfully")
