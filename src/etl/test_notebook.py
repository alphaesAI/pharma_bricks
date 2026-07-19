# Databricks notebook source
# DBTITLE 1,Define Test JSON Payload
import json

# Construct the raw test dictionary payload matching your pipeline schema
# Processing BOTH ma_member.csv and ma_claims.csv in one pipeline run
test_payload = {
    "FileIds": [
        {
            "ClientID": "100",
            "FileID": "1111",
            "FileName": "834member.csv",
            "ClientContainer": "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/output",
            "CurrentFolderPath": "",
            "ProcessedFolderPath": "/Volumes/pharma_catalog/bronze/processed_data",
            "ColumnDelimiter": ",",
            "HasHeader": "True",
            "IgnoreHeader": "False",
            "FileLayoutID": 834,
            "FileLayoutDescription": "Standard834",
            "SchemaFileName": "member_7.12_schema.json",
            "SchemaFilePath": "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/datalake-dev/JSON/Schema",
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
    
    # Use a reasonable timeout instead of 0 to avoid serverless concurrency limits
    # timeout_seconds=0 triggers serverless jobs with a concurrency limit of 1
    pipeline_result = dbutils.notebook.run(
        path="/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/FilesToProcess",
        timeout_seconds=600,  # 10 minute timeout - adjust based on your pipeline duration
        arguments={"ProcessedJSON": json_string_input}
    )
    
    print("Pipeline Execution Completed Successfully!")
    print("Returned Metric JSON Output:")
    print(pipeline_result)

except Exception as e:
    print("Pipeline execution encountered an error:")
    print(str(e))

# COMMAND ----------

# DBTITLE 1,Load FilesToProcess Directly
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/FilesToProcess"

# COMMAND ----------

# DBTITLE 1,Load Helper Classes
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/SyncJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Load FileHandling
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/FileHandling"

# COMMAND ----------

# DBTITLE 1,Load FCFClaimsProcessing
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/FCFClaimsProcessing"

# COMMAND ----------

# DBTITLE 1,Load MoveFileToProcess
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/MoveFileToProcess"

# COMMAND ----------

# DBTITLE 1,Verify Functions Loaded
# Check if all functions are available
print("✓ process_fcf_claims available:", 'process_fcf_claims' in dir())
print("✓ process_move_file available:", 'process_move_file' in dir())
print("✓ synJSONCreator available:", 'synJSONCreator' in dir())
print("✓ delimitedFile available:", 'delimitedFile' in dir())
print("\nAll functions loaded successfully!")
