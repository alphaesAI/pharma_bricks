import json
from src.etl.preprocessing.formatter import TransactionFormatter
from src.etl.preprocessing.parser import EDIParser
from src.etl.preprocessing.mappings.csv_schema_mapper import CSVSchemaMapper
from src.etl.preprocessing.mappings.csv_converter import CSVConverter


def main():
    # 1. Initialize our standard tools (Removed the redundant empty csv_converter initialization)
    parser = EDIParser()
    formatter = TransactionFormatter()
    csv_mapper = CSVSchemaMapper()

    # 2. Parse and structurally format the raw EDI text payload
    print("--- Parsing Raw EDI Data ---")
    generic_json = parser.parse("samples/837_actual_data.txt")
    structured_json = formatter.format(generic_json)

    # 3. Extract demographic information using map_member
    print("\n--- Running Member Profile Mapping ---")
    member_profile = csv_mapper.map_member(structured_json, generic_json)
    
    # 4. Extract billing, provider, and clinical data using map_claims
    print("\n--- Running Outbound Claims Mapping ---")
    claims_profile = csv_mapper.map_claims(structured_json, generic_json)
    
    # 5. Convert to CSV format
    print("\n--- Converting to CSV Format ---")
    # Initialize with the schema directory path
    csv_converter = CSVConverter(schemas_dir="bis-datalake-dev/JSON/Schema")
    
    # Run both conversions explicitly to generate your layout-compliant files
    csv_converter.convert_members(member_profile, "output/src_member_7.12.csv")
    csv_converter.convert_claims(claims_profile, "output/src_claims_7.12.csv")

    # 6. Output both extraction profiles to view details side-by-side
    print("\n================ MEMBER RESULT ================")
    print(json.dumps(member_profile, indent=2))
    
    print("\n================ CLAIMS RESULT ================")
    print(json.dumps(claims_profile, indent=2))


def fileprocessor():
    pass

if __name__ == "__main__":
    main()