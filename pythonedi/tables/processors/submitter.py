from psycopg2.extras import RealDictCursor


class SubmitterProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "submitter" not in mapped_data:
            print("submitter not found")
            return

        submitter = mapped_data["submitter"]

        self.insert(submitter)

    def insert(self, submitter: dict):

        columns = list(submitter.keys())
        values = list(submitter.values())

        print("Columns:", columns)

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO submitter (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT (submitter_id)
        DO NOTHING
        """

        cursor = self.conn.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()

        print("submitter inserted successfully")