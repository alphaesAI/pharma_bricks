import sys
sys.path.append('.')
from pyedi import SchemaMapper

data = {"loops": [{"id": "1", "val": "A"}, {"id": "2", "val": "B"}]}
mapping = {"test1": "loops[0].val", "test2": "loops[?(@.id=='2')].val"}

try:
    mapper = SchemaMapper(mapping)
    res = mapper.map(data)
    print("Result:", res)
except Exception as e:
    print("Error:", e)
