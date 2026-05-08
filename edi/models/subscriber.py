from dataclasses import dataclass


@dataclass
class Subscriber:
    last_name: str = ""
    first_name: str = ""
    member_id: str = ""