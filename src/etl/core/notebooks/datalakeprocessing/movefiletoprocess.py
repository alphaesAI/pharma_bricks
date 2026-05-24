import json
import traceback
import os
from datetime import datetime
from typing import Dict, Any

try:
    import pandas as pd
except ImportError:
    raise ImportError("pandas is required to process dataframes in pure python. Run: pip install pandas pyarrow")

def move_file_to_process(params: Dict[str, Any]) -> str:
    """
    Standard Python equivalent of MoveFileToProcess.scala using Pandas.
    No PySpark, no Databricks dependencies.
    """
    # Setup parameters
    client_id = params.get("ClientID", "")
    file_id = params.get("FileID", "")
    file_layout_id = params.get("FileLayoutID", "")
    file_layout_description = params.get("FileLayoutDescription", "")
    column_delimiter = params.get("ColumnDelimiter", ",")
    
    # Logic for headers
    has_header = str(params.get("HasHeader", "")).capitalize() == "True"
    ignore_header = str(params.get("IgnoreHeader", "True")).capitalize() == "True"
    
    text_qualifier = params.get("TextQualifier", '"')
    if not text_qualifier:
        text_qualifier = '"'  # default fallback
        
    full_file_name = params.get("FullFileName", "")
    processed_path = params.get("ProcessedPath", "")
    
    current_job_id = params.get("jobId", "")
    
    result_json = {
        "CurrentJobId": current_job_id
    }
    
    try:
        if not os.path.exists(full_file_name):
            raise FileNotFoundError(f"File not found: {full_file_name}")

        # Determine header arguments for pandas based on Scala logic
        # if IgnoreHeader=="False" -> keep header (header=0 if has_header else header=None)
        # if IgnoreHeader=="True" && HasHeader=="True" -> skip header row (header=0, but we might skip it or rename)
        if not ignore_header:
            header_arg = 0 if has_header else None
            skiprows = None
        elif ignore_header and has_header:
            # Skip the actual header row but treat data as having no header (columns will be numeric)
            header_arg = None
            skiprows = 1
        else:
            header_arg = None
            skiprows = None

        # Read the file
        df = pd.read_csv(
            full_file_name,
            sep=column_delimiter,
            header=header_arg,
            skiprows=skiprows,
            quotechar=text_qualifier,
            dtype=str, # Read everything as string to prevent data loss/conversion issues like Spark does
            keep_default_na=False
        )
        
        if not df.empty:
            # If header_arg is None, pandas assigns integer column names: 0, 1, 2...
            # The Scala code expected column names to exist to filter 'Filler_'. 
            # If they are integers, we convert them to strings.
            df.columns = [str(c) for c in df.columns]
            
            # Filter out columns starting with 'Filler_'
            cols_to_keep = [c for c in df.columns if not str(c).startswith("Filler_")]
            df = df[cols_to_keep]
            
            # Add file based columns
            df["FILE_ID"] = file_id
            df["FILE_LAYOUT_ID"] = file_layout_id
            df["FILE_LAYOUT_DESCRIPTION"] = file_layout_description
            df["CLIENT_ID"] = client_id
            df["LOAD_DATETIME"] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            
            # Write dataframe to processed path in Parquet format
            # Using append mode equivalent in pandas/pyarrow
            # We save it to a directory just like spark does, partitioning if needed, but here we just append to a file/folder
            os.makedirs(os.path.dirname(processed_path) if os.path.dirname(processed_path) else '.', exist_ok=True)
            
            if os.path.exists(processed_path) and os.path.isdir(processed_path):
                # If it's a directory (like Spark creates), create a new file inside it
                filename = f"part-{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
                output_file = os.path.join(processed_path, filename)
            else:
                # Or just append/write to the specific file
                output_file = processed_path
                # Note: true append to a single parquet file is complex, usually we just write a new file in a directory.
                # If the path isn't a directory but exists, pandas to_parquet doesn't natively append to a single file. 
                # We assume processed_path is a directory for appending parts.
                if not os.path.isdir(processed_path):
                    if not processed_path.endswith('.parquet'):
                        processed_path += '.parquet'
                    output_file = processed_path
            
            # If the user wants to truly append to an existing single parquet file, we'd have to read and concat.
            # But standard data lake pattern is writing new part files into a folder.
            if os.path.exists(output_file) and not os.path.isdir(processed_path):
                # Append to single file
                existing_df = pd.read_parquet(output_file)
                df = pd.concat([existing_df, df], ignore_index=True)
                
            df.to_parquet(output_file, engine='pyarrow', index=False)
            
            result_json["Status"] = "SUCCESS"
            result_json["ProcessedCount"] = str(len(df))
            result_json["ErrorMessage"] = ""
        else:
            result_json["Status"] = "SUCCESS"
            result_json["ProcessedCount"] = "0"
            result_json["ErrorMessage"] = ""
            
    except Exception as e:
        result_json["Status"] = "FAILED"
        result_json["ProcessedCount"] = "0"
        err_msg = str(e).replace('"', '').replace('\n', ' ').replace('\r', '')
        result_json["ErrorMessage"] = err_msg
        
    return json.dumps(result_json)

if __name__ == "__main__":
    # Example usage for local testing
    sample_params = {
        "ClientID": "CLIENT123",
        "FileID": "101",
        "FullFileName": "sample.csv",
        "ProcessedPath": "output_dir",
        "ColumnDelimiter": ",",
        "HasHeader": "True",
        "IgnoreHeader": "False"
    }
    # print(move_file_to_process(sample_params))
