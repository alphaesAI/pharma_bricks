from dataclasses import dataclass


@dataclass
class Claim:
    claim_id: str = ""
    amount: str = ""