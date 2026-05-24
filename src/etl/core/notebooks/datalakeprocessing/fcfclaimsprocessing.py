import json
import traceback
import os
from datetime import datetime
from typing import Dict, Any

try:
    import pandas as pd
    import numpy as np
except ImportError:
    raise ImportError("pandas and numpy are required to process dataframes in pure python. Run: pip install pandas numpy pyarrow")

def process_fcf_claims(params: Dict[str, Any]) -> str:
    """
    Standard Python equivalent of FCFClaimsProcessing.scala using Pandas.
    No PySpark, no Databricks dependencies.
    """
    # Setup parameters
    client_id = params.get("ClientID", "")
    file_id = params.get("FileID", "")
    file_layout_id = params.get("FileLayoutID", "")
    file_layout_description = params.get("FileLayoutDescription", "")
    column_delimiter = params.get("ColumnDelimiter", ",")
    has_header = str(params.get("HasHeader", "")).capitalize() == "True"
    ignore_header = str(params.get("IgnoreHeader", "True")).capitalize() == "True"
    
    full_file_name = params.get("FullFileName", "")
    schema_file = params.get("SchemaFile", "")
    processed_path = params.get("ProcessedPath", "")
    
    current_job_id = params.get("jobId", "")
    
    result_json = {
        "CurrentJobId": current_job_id
    }
    
    try:
        if not os.path.exists(full_file_name):
            raise FileNotFoundError(f"File not found: {full_file_name}")

        # In Scala, it reads the schema from a json file to get column names, but for pandas 
        # we can just read the header from the CSV directly or provide names if no header.
        # If schema_file is provided and parseable, one would load names. Here we assume
        # the file has headers or we skip the schema reading complexity for standard csv loading.
        
        header_arg = 0 if has_header else None
        
        df = pd.read_csv(
            full_file_name,
            sep=column_delimiter,
            header=header_arg,
            dtype=str, # Read as string initially
            keep_default_na=False
        )
        
        if not df.empty:
            # 1. Trim whitespaces for all columns
            df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            
            # 2. Add New Columns
            df["FILE_ID"] = file_id
            df["FILE_LAYOUT_ID"] = file_layout_id
            df["FILE_LAYOUT_DESCRIPTION"] = file_layout_description
            df["CLIENT_ID"] = client_id
            
            # IS_SPLIT_CLAIM
            if "MA_SPLIT_CLAIM_ID" in df.columns:
                is_empty = df["MA_SPLIT_CLAIM_ID"].isna() | (df["MA_SPLIT_CLAIM_ID"] == "")
                df["IS_SPLIT_CLAIM"] = np.where(is_empty, 0, 1)
            else:
                df["IS_SPLIT_CLAIM"] = 0
                
            # CLAIM_WEIGHT
            if "MA_CLAIM_STATUS" in df.columns and "MA_CLAIM_UPDATED_DT" in df.columns:
                status = df["MA_CLAIM_STATUS"].str.upper()
                weight_base = np.select(
                    [status == "6", status == "C", status == "8", status == "O"], 
                    [7, 7, 5, 1], 
                    default=0
                )
                
                update_dt = pd.to_datetime(df["MA_CLAIM_UPDATED_DT"], format="%m/%d/%Y %H:%M:%S", errors='coerce')
                base_dt = pd.to_datetime("01/01/2016 00:00:00", format="%m/%d/%Y %H:%M:%S")
                dt_diff = (update_dt - base_dt).dt.total_seconds() * 10
                dt_diff = dt_diff.fillna(0)
                
                df["CLAIM_WEIGHT"] = weight_base + dt_diff
            
            # MA_CLAIM_ID_ORIG for split claim
            if "MA_CLAIM_ID_ORIG" in df.columns and "MA_CLAIM_NUM" in df.columns:
                df["MA_CLAIM_ID_ORIG"] = np.where(
                    df["IS_SPLIT_CLAIM"] == 1, 
                    df["MA_CLAIM_NUM"], 
                    df["MA_CLAIM_ID_ORIG"]
                )
                
            # Date conversions based on the Scala script (convert to date/timestamp)
            date_cols = [
                "MA_PATIENT_DOB", "MA_BEGINNING_DOS", "MA_CHECK_DATE", "MA_FINALIZED_FILE_CREATE_DATE",
                "MA_CLAIM_RECEIVE_DATE", "MA_CLAIM_FINALIZED_DT", "MA_SUBCRIBER_BIRTH_DATE",
                "MA_BENEFIT_PERIOD_BEGIN_DT", "MA_BENEFIT_PERIOD_END_DT", "MA_PATIENT_CURRENT_ILLNESS_DT",
                "MA_PATIENT_SIMILAR_ILLNESS_DT", "MA_PATIENT_LAST_WORKED_DT", "MA_PATIENT_RETURN_WORK_DT",
                "MA_CLAIM_HOSP_ADMIT_DT", "MA_CLAIM_HOSP_DISCHARGE_DT", "MA_STATEMENT_FROM_DT",
                "MA_STATEMENT_TO_DT", "MA_CLAIM_PRIM_PROC_DT", "MA_ITS_CLM_RF_POST_DT", "MA_CLM_BACKOUT_DT",
                "MA_LINE_SERVICE_FROM_DT", "MA_LINE_SERVICE_TO_DT", "MA_LINE_GL_DT"
            ]
            # Add OCCUR and OCCUR_SPAN date fields up to 24
            for i in range(1, 25):
                date_cols.append(f"MA_CLAIM_OCCUR_DT{i}")
                date_cols.append(f"MA_CLAIM_OCCUR_SPAN_FROM_DT{i}")
                date_cols.append(f"MA_CLAIM_OCCUR_SPAN_TO_DT{i}")
                date_cols.append(f"MA_CLAIM_OTHER_PROC_DT_{i}")
                
            for col in date_cols:
                if col in df.columns:
                    # Convert to datetime date format
                    df[col] = pd.to_datetime(df[col], format="%m/%d/%Y", errors='coerce').dt.date

            # Timestamp conversions
            ts_cols = ["MA_CLAIM_ENTRY_DT", "MA_CLAIM_UPDATED_DT"]
            for col in ts_cols:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], format="%m/%d/%Y %H:%M:%S", errors='coerce')
            
            # --- DELINK CLAIMS LOGIC ---
            if "MA_CLAIM_STATUS" in df.columns and "MA_CLAIM_NUM" in df.columns:
                prev_status = df.get("MA_CLAIM_STATUS_PREV", pd.Series([""] * len(df)))
                
                status_cond = (df["MA_CLAIM_STATUS"] == "8") | ((df["MA_CLAIM_STATUS"] == "O") & (prev_status == "8"))
                
                event_cond = pd.Series([False] * len(df), index=df.index)
                for i in range(1, 15):
                    col_name = f"MA_LINE_EVENT_CD{i}"
                    if col_name in df.columns:
                        event_cond = event_cond | df[col_name].isin(["502", "505", "611"])
                        
                is_not_split = df["IS_SPLIT_CLAIM"] != 1
                
                is_denied = status_cond & event_cond & is_not_split
                df["IS_DENIED_DUPLICATE"] = np.where(is_denied, 1, 0)
                
                # Unlink
                df["MA_CLAIM_ID_ORIG"] = np.where(
                    df["IS_DENIED_DUPLICATE"] == 1, 
                    df["MA_CLAIM_NUM"], 
                    df["MA_CLAIM_ID_ORIG"]
                )
            
            # --- FINAL KEYS & SAVING ---
            df["GENERATED_CLAIMS_UNIQUE_KEY"] = df.get("MA_LINE_CLAIM_NUM", "") + "-" + file_id + "-" + client_id
            df["GENERATED_GOLDEN_CLAIMS_UNIQUE_KEY"] = df.get("MA_CLAIM_ID_ORIG", "") + "-" + file_layout_id + "-" + client_id
            df["LOAD_DATETIME"] = pd.to_datetime(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
            
            if "MA_LINE_SERVICE_FROM_DT" in df.columns:
                df["PARTITION_KEY"] = pd.to_datetime(df["MA_LINE_SERVICE_FROM_DT"]).dt.year
            else:
                df["PARTITION_KEY"] = datetime.now().year
                
            # Drop any rows where PARTITION_KEY became NA/NaN due to missing dates
            df["PARTITION_KEY"] = df["PARTITION_KEY"].fillna(1900).astype(int)

            # Write dataframe to processed path in Parquet format, partitioned
            os.makedirs(os.path.dirname(processed_path) if os.path.dirname(processed_path) else '.', exist_ok=True)
            
            # Using pyarrow directly or pandas to_parquet for partitioned write
            # Pandas supports partition_cols
            df.to_parquet(
                processed_path, 
                engine='pyarrow', 
                partition_cols=['PARTITION_KEY'],
                index=False
            )
            
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
    # print(process_fcf_claims(sample_params))
