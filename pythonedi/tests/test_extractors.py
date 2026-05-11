from ..parsers.edi_parser import EDIParser
from ..services.loop_context_service import LoopContextService


parser = EDIParser()
xml_root = parser.parse("samples/837_actual_data.txt")

contexts = LoopContextService(xml_root).build_contexts()

assert "2000A" in contexts
assert "2000B" in contexts
assert "2300" in contexts