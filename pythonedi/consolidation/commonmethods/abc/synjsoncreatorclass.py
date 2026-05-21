class SynJSONCreator:
    """
    Python equivalent of SynJSONCreatorClass.scala.
    Provides standard JSON string building primitives matching Databricks notebook calls.
    """

    def __init__(self):
        self.json_str = ""
        self.double_quote = '"'

    def addBracketStart(self):
        self.json_str += "["

    def addBracketEnd(self):
        self.json_str += "]"

    def addBraceStart(self):
        self.json_str += "{"

    def addBraceEnd(self):
        self.json_str += "}"

    def addComma(self):
        self.json_str += ","

    def addNewEntry(self, key: str, value: str, newLine: bool = True):
        # Escape quotes inside value if present
        safe_value = str(value).replace('"', '\\"')
        self.json_str += f'{self.double_quote}{key}{self.double_quote}:{self.double_quote}{safe_value}{self.double_quote}'
        if newLine:
            self.json_str += ","

    def getJSON(self) -> str:
        return self.json_str
