from psycopg2.extras import RealDictCursor


class PayerProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "payer" not in mapped_data:
            print("payer not found")
            return

        payer = mapped_data["payer"]
        self.insert(payer)

    def insert(self, payer: dict):

        columns = list(payer.keys())
        print("Columns:", columns)

        values = list(payer.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO payer (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT (payer_id) 
        DO NOTHING
        """

        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

        print("payer inserted successfully")
