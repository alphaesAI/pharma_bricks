from psycopg2.extras import RealDictCursor


class ServiceLineProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "service_line" not in mapped_data:
            print("service_line not found")
            return

        service_line = mapped_data["service_line"]
        self.insert(service_line)

    def insert(self, service_line: dict):

        columns = list(service_line.keys())
        print("Columns:", columns)

        values = list(service_line.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO service_line (
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

        print("service_line inserted successfully")
