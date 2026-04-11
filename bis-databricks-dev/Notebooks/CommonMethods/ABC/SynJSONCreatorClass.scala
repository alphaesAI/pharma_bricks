// Databricks notebook source
class synJSONCreator {
  var JSON = ""
  val doubleQuote = """ " """.trim()
  
  def addBracketStart() {
    JSON += "["
  }
  
  def addBracketEnd() {
    JSON += "]"
  }
  
  def addBraceStart() {
    JSON += "{"
  }
  
  def addBraceEnd() {
    JSON += "}"
  }
  
  def addComma() {
    JSON += ","
  }
  
  def addNewEntry (key: String, value: String, newLine: Boolean = true) {
    JSON += doubleQuote + key  + doubleQuote + ":"  + doubleQuote + value + doubleQuote 
    if (newLine) {JSON += ","}
  }
  
  def getJSON(): String = {
    return JSON
  }
  
}