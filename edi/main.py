from .parsers.edi_parser import EDIParser
from .services.loop_context_service import LoopContextService
from .extractors.provider_extractor import ProviderExtractor
from .extractors.subscriber_extractor import SubscriberExtractor
from .extractors.claim_extractor import ClaimExtractor
from .services.merge_service import MergeService


def main():
    parser = EDIParser()

    xml_root = parser.parse("samples/837_actual_data.txt")

    context_service = LoopContextService(xml_root)
    contexts = context_service.build_contexts()

    provider = ProviderExtractor().extract(contexts)
    subscriber = SubscriberExtractor().extract(contexts)
    claims = ClaimExtractor().extract(contexts)

    merged = MergeService().merge(
        provider=provider,
        subscriber=subscriber,
        claims=claims
    )

    print(merged)


if __name__ == "__main__":
    main()