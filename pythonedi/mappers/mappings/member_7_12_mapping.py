"""
Declarative pyedi Mapping Definition matching member_7.12 JSON Schema
"""

MEMBER_7_12_MAPPING_DEFINITION = {
    "name": "Member 7.12 Schema Mapping",
    "mapping_type": "only_mapped",

    "expressions": {
        "TEMPLATE": "detail.unmapped",
        
        # Core mapped demographics from Subscriber Loop (2010BA)
        "UNIQUEPERSONKEY": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",
        "BENEFICIARYID": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",
        "MEDICAIDID": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",
        "LASTNAME": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_last_name",
        "FIRSTNAME": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_first_name",
        "MIDDLEINITIAL": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_middle_name",
        "DATEOFBIRTH": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_birth_date",
        "GENDER": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_gender_code",
        
        # Permanent Address Information
        "PERMANENTADDRESSLINE1": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_1",
        "PERMANENTADDRESSLINE2": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_2",
        "PERMANENTCITY": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_city",
        "PERMANENTSTATE": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_state",
        "PERMANENTZIPCODE": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_zip_code",
        "PERMANENTCOUNTY": "detail.unmapped",
        
        # Communication (Mapped to Subscriber contact segment PER[1])
        "TELEPHONENUMBER": "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_04",
        "EMAIL": "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_06",
        "FAX": "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_08",
        
        # Mailing Address
        "MAILINGADDRESSLINE1": "detail.unmapped",
        "MAILINGADDRESSLINE2": "detail.unmapped",
        "MAILINGCITY": "detail.unmapped",
        "MAILINGSTATE": "detail.unmapped",
        "MAILINGZIPCODE": "detail.unmapped",
        "MAILINGCOUNTY": "detail.unmapped",
        
        # Caretaker Info
        "CARETAKERFIRSTNAME": "detail.unmapped",
        "CARETAKERLASTNAME": "detail.unmapped",
        "CARETAKERMIDDLEINITIAL": "detail.unmapped",
        
        # Demographics details
        "RACE": "detail.unmapped",
        "RACEDATASOURCE": "detail.unmapped",
        "ETHNICITY": "detail.unmapped",
        "ETHNICITYDATASOURCE": "detail.unmapped",
        
        # Languages
        "SPOKENLANGUAGE": "detail.unmapped",
        "SPOKENLANGUAGESOURCE": "detail.unmapped",
        "WRITTENLANGUAGE": "detail.unmapped",
        "WRITTENLANGUAGESOURCE": "detail.unmapped",
        "OTHERLANGUAGE": "detail.unmapped",
        "OTHERLANGUAGESOURCE": "detail.unmapped",
        
        # Identifiers & Attributes
        "USCITIZEN": "detail.unmapped",
        "DECEASEDDATE": "detail.unmapped",
        "MASKEDMEMBERID": "detail.unmapped",
        "ENROLLEEEDUCATION": "detail.unmapped",
        "ENROLLEEEMPLOYMENT": "detail.unmapped",
        
        # Alternate Keys
        "ALTERNATEKEY1": "detail.unmapped",
        "ALTERNATEKEY2": "detail.unmapped",
        "ALTERNATEKEY3": "detail.unmapped",
        "ALTERNATEKEY4": "detail.unmapped",
        "ALTERNATEKEY5": "detail.unmapped",
        "ALTERNATEKEY6": "detail.unmapped",
        "ALTERNATEKEY7": "detail.unmapped",
        "ALTERNATEKEY8": "detail.unmapped",
        "ALTERNATEKEY9": "detail.unmapped",
        "ALTERNATEKEY10": "detail.unmapped"
    }
}
