from psycopg2.extras import RealDictCursor


class SubscriberProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        # -----------------------------------
        # isolate
        # -----------------------------------
        if "subscriber" not in mapped_data:
            print("subscriber not found")
            return

        subscriber = mapped_data["subscriber"]

        # -----------------------------------
        # persist
        # -----------------------------------
        self.insert(subscriber)

    def insert(self, subscriber: dict):

        columns = list(subscriber.keys())
        print("Columns:", columns)

        values = list(subscriber.values())

        column_string = ", ".join(columns)

        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO subscriber (
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

        print("subscriber inserted successfully")