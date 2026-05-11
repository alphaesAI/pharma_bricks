from psycopg2.extras import RealDictCursor


class ClaimProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "claim" not in mapped_data:
            print("claim not found")
            return

        claim = mapped_data["claim"]
        self.insert(claim)

    def insert(self, claim: dict):

        columns = list(claim.keys())
        print("Columns:", columns)

        values = list(claim.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO claim (
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

        print("claim inserted successfully")
