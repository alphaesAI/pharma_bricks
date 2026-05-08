class MergeService:

    def merge(self, provider, subscriber, claims):

        return {
            "provider": provider.__dict__,
            "subscriber": subscriber.__dict__,
            "claims": [claim.__dict__ for claim in claims]
        }