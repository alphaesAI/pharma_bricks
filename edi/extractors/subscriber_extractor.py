from .base import BaseExtractor
from ..models.subscriber import Subscriber


class SubscriberExtractor(BaseExtractor):

    def extract(self, contexts):
        subscriber_data = {}

        for segment in contexts["2000B"]:

            if segment.tag == "NM1":
                subscriber_data["last_name"] = segment.findtext("NM103")
                subscriber_data["first_name"] = segment.findtext("NM104")
                subscriber_data["member_id"] = segment.findtext("NM109")

        return Subscriber(**subscriber_data)