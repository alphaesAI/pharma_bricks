from psycopg2.extras import RealDictCursor


class InterchangeProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "interchange" not in mapped_data:
            print("interchange not found")
            return

        interchange = mapped_data["interchange"]
        self.insert(interchange)

    def insert(self, interchange: dict):

        columns = list(interchange.keys())
        print("Columns:", columns)

        values = list(interchange.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO interchange (
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

        print("interchange inserted successfully")
