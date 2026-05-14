from psycopg2.extras import RealDictCursor


class InterchangeProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        # -----------------------------------
        # isolate
        # -----------------------------------
        if "interchange" not in mapped_data:
            print("interchange not found")
            return

        interchange = mapped_data["interchange"]

        # -----------------------------------
        # persist
        # -----------------------------------
        self.insert(interchange)

    def insert(self, interchange: dict):

        columns = list(interchange.keys())
        values = list(interchange.values())

        print("Columns:", columns)

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO interchange (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT (control_number)
        DO NOTHING
        """

        cursor = self.conn.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()

        print("interchange inserted successfully")