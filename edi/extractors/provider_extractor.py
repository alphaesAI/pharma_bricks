from .base import BaseExtractor
from ..models.provider import Provider


class ProviderExtractor(BaseExtractor):

    def extract(self, contexts):
        provider_data = {}

        for segment in contexts["2000A"]:

            if segment.tag == "NM1":
                provider_data["name"] = segment.findtext("NM103")
                provider_data["id"] = segment.findtext("NM109")

        return Provider(**provider_data)