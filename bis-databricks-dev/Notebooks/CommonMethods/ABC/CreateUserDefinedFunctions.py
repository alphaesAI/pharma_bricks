# Databricks notebook source
# DBTITLE 1,Overpunch Function
def overpunchUDF(overpunchString):
  tempOverPunchString = overpunchString
  lastChar = tempOverPunchString[-1]
  firstChar = tempOverPunchString[0]
  lengthMinusLastChar = len(tempOverPunchString) - 1

  if lastChar == "{":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '0'
  elif lastChar == "}":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '0'
  elif lastChar == "A":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '1'
  elif lastChar == "J":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '1'
  elif lastChar == "B":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '2'
  elif lastChar == "K":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '2'
  elif lastChar == "C":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '3'
  elif lastChar == "L":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '3'
  elif lastChar == "D":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '4'
  elif lastChar == "M":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '4'
  elif lastChar == "E":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '5'
  elif lastChar == "N":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '5'
  elif lastChar == "F":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '6'
  elif lastChar == "O":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '6'
  elif lastChar == "G":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '7'
  elif lastChar == "P":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '7'
  elif lastChar == "H":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '8'
  elif lastChar == "Q":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '8'
  elif lastChar == "I":
    tempOverPunchString = firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '9'
  elif lastChar == "R":
    tempOverPunchString = '-' + firstChar + tempOverPunchString[1:lengthMinusLastChar]  +  '9'
  else:
    tempOverPunchString = tempOverPunchString
  
  returnVariable = None
  
  try:
      returnVariable = int(tempOverPunchString)
  except ValueError:
      returnVariable = None

  return returnVariable

# COMMAND ----------

# DBTITLE 1,Register Overpunch UDF
overpunch = udf(overpunchUDF)
spark.udf.register("overpunch", overpunchUDF)
