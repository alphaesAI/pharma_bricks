from psycopg2.extras import RealDictCursor


class ClaimProcessor:

    def __init__(self, conn):
        self.conn = conn

    def process(self, mapped_data: dict):

        # -----------------------------------
        # isolate
        # -----------------------------------
        if "claim" not in mapped_data:
            print("claim not found")
            return

        claim = mapped_data["claim"]

        if "subscriber" in mapped_data:
            claim["subscriber_id"] = mapped_data["subscriber"].get("subscriber_id")

        if "billing_provider" in mapped_data:
            claim["billing_provider_id"] = mapped_data["billing_provider"].get("billing_provider_npi")

        if "payer" in mapped_data:
            claim["payer_id"] = mapped_data["payer"].get("payer_id")

        # -----------------------------------
        # persist (Handling single or multiple claims)
        # -----------------------------------
        claim_numbers = claim.get("claim_number")
        if isinstance(claim_numbers, list):
            num_claims = len(claim_numbers)
            for i in range(num_claims):
                single_claim = {}
                for key, val in claim.items():
                    if isinstance(val, list) and len(val) == num_claims:
                        single_claim[key] = val[i]
                    elif isinstance(val, list):
                        single_claim[key] = val[i] if i < len(val) else None
                    else:
                        single_claim[key] = val
                self.insert(single_claim)
        else:
            self.insert(claim)

    def insert(self, claim: dict):

        columns = list(claim.keys())
        values = list(claim.values())

        print("Columns:", columns)

        column_string = ", ".join(columns)
        placeholder_string = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO claim (
            {column_string}
        )
        VALUES (
            {placeholder_string}
        )
        ON CONFLICT (claim_number) 
        DO NOTHING
        """

        cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()

        print("claim inserted successfully")