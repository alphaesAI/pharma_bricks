from psycopg2.extras import RealDictCursor


class ClaimDatesProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "claim_dates" not in mapped_data:
            print("claim_dates not found")
            return

        claim_dates = mapped_data["claim_dates"]
        self.insert(claim_dates)

    def insert(self, claim_dates: dict):

        columns = list(claim_dates.keys())
        print("Columns:", columns)

        values = list(claim_dates.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO claim_dates (
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

        print("claim_dates inserted successfully")
