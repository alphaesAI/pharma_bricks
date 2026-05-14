from psycopg2.extras import RealDictCursor


class ReceiverProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        if "receiver" not in mapped_data:
            print("receiver not found")
            return

        receiver = mapped_data["receiver"]
        self.insert(receiver)

    def insert(self, receiver: dict):

        columns = list(receiver.keys())
        print("Columns:", columns)

        values = list(receiver.values())

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO receiver (
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

        print("receiver inserted successfully")
