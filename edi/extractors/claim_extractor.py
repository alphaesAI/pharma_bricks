from .base import BaseExtractor
from ..models.claim import Claim


class ClaimExtractor(BaseExtractor):

    def extract(self, contexts):
        claims = []

        for segment in contexts["2300"]:

            if segment.tag == "CLM":
                claim = Claim(
                    claim_id=segment.findtext("CLM01"),
                    amount=segment.findtext("CLM02")
                )

                claims.append(claim)

        return claims