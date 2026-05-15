import requests
import json

# Define the Stedi API Endpoint for reading raw EDI data
STEDI_URL = "https://stedi.com"
API_KEY = "YOUR_STEDI_PRODUCTION_OR_TEST_API_KEY"

# Your raw inbound X12 EDI text file data string
raw_edi_input = """ISA*00*          *00*          *ZZ*SENDERGS       *ZZ*RECEIVERGS     *260515*1341*^*00501*000000001*0*T*:~GS*HC*SENDERGS*RECEIVERGS*20260515*1341*1*X*005010X222A1~ST*837*0001*005010X222A1~BHT*0019*00*012345*20260515*1341*CH~HL*1**20*1~NM1*85*2*CLINIC HEALTH*****XX*1234567890~HL*2*1*22*0~NM1*IL*1*SMITH*JOHN****MI*A12345678~CLM*CLAIM999*150.00***11:B:1*Y*A*Y*Y~SE*8*0001~GE*1*1~IEA*1*000000001~"""

headers = {
    "Authorization": f"Key {API_KEY}",
    "Content-Type": "text/plain"
}

# Execute the dynamic conversion request
response = requests.post(STEDI_URL, headers=headers, data=raw_edi_input)

if response.status_code == 200:
    human_readable_json = response.json()
    print(json.dumps(human_readable_json, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
