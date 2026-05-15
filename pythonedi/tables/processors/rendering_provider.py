from psycopg2.extras import RealDictCursor


class RenderingProviderProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        # -----------------------------------
        # isolate
        # -----------------------------------
        if "rendering_provider" not in mapped_data:
            print("rendering_provider not found")
            return

        rendering_provider = mapped_data["rendering_provider"]

        # -----------------------------------
        # inject foreign key
        # -----------------------------------
        if "claim" in mapped_data:
            rendering_provider["claim_number"] = (
                mapped_data["claim"]["claim_number"]
            )

        # -----------------------------------
        # persist
        # -----------------------------------
        self.insert(rendering_provider)

    def insert(self, rendering_provider: dict):

        columns = list(rendering_provider.keys())
        values = list(rendering_provider.values())

        print("Columns:", columns)

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO rendering_provider (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT (rendering_provider_npi) 
        DO NOTHING
        """

        cursor = self.conn.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()

        print("rendering_provider inserted successfully")