from claim_box.consolidation.parser import X12Parser
from claim_box.consolidation.csv_writer import CSVWriter


def run():
    # Paths
    input_file = "execution/samples/837_mult_claims.txt"
    config_file = "claim_box/config/csv_extraction_bis.json"
    output_dir = "output"

    try:
        # Step 1: Parse EDI to segments
        parser = X12Parser(input_file)
        segments = parser()
        print(f"Parsed {len(segments)} segments")

        # Step 2: Write CSV files
        writer = CSVWriter(config_file, output_dir)
        writer(segments)

    except Exception as e:
        print(f"Orchestrator Error: {e}")
        raise


if __name__ == "__main__":
    run()