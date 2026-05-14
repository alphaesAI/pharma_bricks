from psycopg2.extras import RealDictCursor


class FunctionalGroupProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "functional_group" not in mapped_data:
            print("functional_group not found")
            return

        functional_group = mapped_data["functional_group"]
        self.insert(functional_group)

    def insert(self, functional_group: dict):

        columns = list(functional_group.keys())
        print("Columns:", columns)

        values = list(functional_group.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO functional_group (
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

        print("functional_group inserted successfully")
