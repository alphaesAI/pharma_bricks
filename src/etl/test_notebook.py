# Databricks notebook source
# DBTITLE 1,Define Test JSON Payload
import json

# Construct the raw test dictionary payload matching your pipeline schema
test_payload = {
    "FileIds": [
        {
            "ClientID": "101",
            "FileID": "9901",
            "FileName": "sample_claims.csv",
            "ClientContainer": "pharma-data-container",
            "CurrentFolderPath": "/landing",
            "ProcessedFolderPath": "/archive",
            "ColumnDelimiter": ",",
            "HasHeader": "true",
            "IgnoreHeader": "false",
            "FileLayoutID": "5001",
            "FileLayoutDescription": "FCF",
            "SchemaFileName": "fcf_claims_schema.json",
            "SchemaFilePath": "/metadata/schemas",
            "TextQualifier": "\""
        }
    ]
}

# Convert the Python dictionary into a single compressed JSON text string
json_string_input = json.dumps(test_payload)

# COMMAND ----------

# DBTITLE 1,Execute Target Notebook Pipeline
try:
    print("Starting pipeline test execution...")
    
    # Navigates from src/tests/etl/preprocessing/ up to src/ and down into the target dev directory
    pipeline_result = dbutils.notebook.run(
        path="./databricks-dev/Notebooks/DatalakeProcessing/FilesToProcess",
        timeout_seconds=1800, 
        arguments={"ProcessedJSON": json_string_input}
    )
    
    print("Pipeline Execution Completed Successfully!")
    print("Returned Metric JSON Output:")
    print(pipeline_result)

except Exception as e:
    print("Pipeline execution encountered an error:")
    print(str(e))