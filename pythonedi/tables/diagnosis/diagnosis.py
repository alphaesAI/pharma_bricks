from psycopg2.extras import RealDictCursor


class DiagnosisProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "diagnosis" not in mapped_data:
            print("diagnosis not found")
            return

        diagnosis = mapped_data["diagnosis"]
        self.insert(diagnosis)

    def insert(self, diagnosis: dict):

        columns = list(diagnosis.keys())
        print("Columns:", columns)

        values = list(diagnosis.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO diagnosis (
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

        print("diagnosis inserted successfully")
