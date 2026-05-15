# dummy

import xml.etree.ElementTree as ET
from pyx12.x12file import X12Reader
from pyx12.errors import X12Error
import io

raw_edi_input = "ISA*00*          *00*          *ZZ*SENDERGS       *ZZ*RECEIVERGS     *260515*1341*^*00501*000000001*0*T*:~GS*HC*SENDERGS*RECEIVERGS*20260515*1341*1*X*005010X222A1~ST*837*0001*005010X222A1~BHT*0019*00*012345*20260515*1341*CH~HL*1**20*1~NM1*85*2*CLINIC HEALTH*****XX*1234567890~HL*2*1*22*0~NM1*IL*1*SMITH*JOHN****MI*A12345678~CLM*CLAIM999*150.00***11:B:1*Y*A*Y*Y~SE*8*0001~GE*1*1~IEA*1*000000001~"

# Setup pyx12 source streams
source_stream = io.StringIO(raw_edi_input)

try:
    # Instantiate the standard X12 parser context engine
    reader = X12Reader(source_stream)
    
    # Iterate dynamically through all segmented loops
    for segment in reader:
        # Elements are exposed as objects matching official X12 descriptions natively
        if segment.get_seg_id() == 'CLM':
            print(f"Segment: {segment.get_seg_id()}")
            print(f"  Claim Submitter Identifier [CLM01]: {segment.get_element(1)}")
            print(f"  Monetary Amount [CLM02]: {segment.get_element(2)}")
            
        elif segment.get_seg_id() == 'NM1':
            print(f"Segment: {segment.get_seg_id()}")
            print(f"  Name Last or Organization Name [NM103]: {segment.get_element(3)}")

except X12Error as e:
    print(f"EDI Validation or Parsing Error: {e}")
