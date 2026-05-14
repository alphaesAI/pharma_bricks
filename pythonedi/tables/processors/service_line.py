from psycopg2.extras import RealDictCursor


class ServiceLineProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        # -----------------------------------
        # isolate
        # -----------------------------------
        if "service_line" not in mapped_data:
            print("service_line not found")
            return

        service_line = mapped_data["service_line"]

        # -----------------------------------
        # inject foreign key
        # -----------------------------------
        if "claim" in mapped_data:
            service_line["claim_number"] = (
                mapped_data["claim"]["claim_number"]
            )

        # -----------------------------------
        # persist
        # -----------------------------------
        self.insert(service_line)

    def insert(self, service_line: dict):

        columns = list(service_line.keys())
        values = list(service_line.values())

        print("Columns:", columns)

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO service_line (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT DO NOTHING
        """

        cursor = self.conn.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()

        print("service_line inserted successfully")