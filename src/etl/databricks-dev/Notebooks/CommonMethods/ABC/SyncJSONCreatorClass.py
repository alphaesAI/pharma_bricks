# Databricks notebook source
class synJSONCreator:
    def __init__(self):
        self.JSON = ""
        self.doubleQuote = '"'
        
    def addBracketStart(self):
        self.JSON += "["
        
    def addBracketEnd(self):
        self.JSON += "]"
        
    def addBraceStart(self):
        self.JSON += "{"
        
    def addBraceEnd(self):
        self.JSON += "}"
        
    def addComma(self):
        self.JSON += ","
        
    def addNewEntry(self, key: str, value: str, newLine: bool = True):
        self.JSON += self.doubleQuote + key + self.doubleQuote + ":" + self.doubleQuote + value + self.doubleQuote 
        if newLine:
            self.JSON += ","
            
    def getJSON(self) -> str:
        return self.JSON