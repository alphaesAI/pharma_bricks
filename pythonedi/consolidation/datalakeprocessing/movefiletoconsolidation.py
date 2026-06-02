# pythonedi/consolidation/move_file_to_consolidation.py
import json
import pandas as pd
import logging
from typing import Dict, List
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MoveFileToConsolidation:
    """
    Process files from processed zone to consolidated zone.
    Reads Parquet, applies schema from JSON, writes to consolidated output.
    Replaces MoveFileToConsolidation.scala
    """
    
    def __init__(self):
        self.job_id = str(datetime.now().timestamp())
    
    def process(self,
                file_id: str,
                current_container: str,
                current_folder_path: str,
                consolidated_layer_data_model: str,
                consolidated_layer_data_model_filepath: str,
                consolidated_mapping_file_name: str,
                consolidated_mapping_file_path: str,
                consolidated_folder_path: str) -> Dict:
        """
        Main consolidation process.
        
        Args:
            file_id: File ID to process
            current_container: Container/client code
            current_folder_path: Path to processed files
            consolidated_layer_data_model: Data model filename
            consolidated_layer_data_model_filepath: Path to data model
            consolidated_mapping_file_name: Mapping filename
            consolidated_mapping_file_path: Path to mapping
            consolidated_folder_path: Output path for consolidated data
            
        Returns:
            Result dictionary with status and record count
        """
        result = {
            "CurrentJobId": self.job_id,
            "ConsolidatedCount": 0,
            "Status": "SUCCESS",
            "ErrorMessage": ""
        }
        
        try:
            # Build full paths
            mount_point = "/mnt/"
            full_processed = f"{mount_point}{current_container}{current_folder_path}/"
            full_consolidated_folder_path = f"{mount_point}{consolidated_folder_path}/"
            data_model_file = f"{mount_point}{consolidated_layer_data_model_filepath}/{consolidated_layer_data_model}"
            consolidation_mapping = f"{mount_point}{consolidated_mapping_file_path}/{consolidated_mapping_file_name}"
            
            logger.info(f"Processing from: {full_processed}")
            logger.info(f"Output to: {full_consolidated_folder_path}")
            
            # Load data model JSON
            with open(data_model_file, 'r') as f:
                data_model_config = json.load(f)
            
            # Load mapping JSON
            with open(consolidation_mapping, 'r') as f:
                mapping_config = json.load(f)
            
            # Build schema from data model
            schema = self._build_schema_from_datamodel(data_model_config)
            
            # Read parquet file
            df_file = pd.read_parquet(full_processed)
            logger.info(f"Read {len(df_file)} rows from parquet")
            
            # Apply mappings and transformations
            df_file_reformatted = self._apply_mappings(df_file, mapping_config, file_id)
            
            # Ensure all required columns exist (null fill missing)
            df_file_final = self._custom_select(df_file_reformatted, schema)
            
            # Write to consolidated (append mode)
            self._write_consolidated(df_file_final, full_consolidated_folder_path)
            
            result["ConsolidatedCount"] = len(df_file_final)
            result["Status"] = "SUCCESS"
            
            logger.info(f"Successfully consolidated {len(df_file_final)} records")
            
        except Exception as e:
            logger.error(f"Error in consolidation: {str(e)}")
            result["Status"] = "FAILED"
            result["ConsolidatedCount"] = 0
            result["ErrorMessage"] = str(e)
        
        return result
    
    def _build_schema_from_datamodel(self, data_model_config: Dict) -> List[str]:
        """Extract field names from data model."""
        fields = data_model_config.get("Fields", [])
        return [field["FieldName"] for field in fields]
    
    def _apply_mappings(self, df: pd.DataFrame, mapping_config: Dict, file_id: str) -> pd.DataFrame:
        """
        Apply column mappings and transformations from mapping JSON.
        
        Handles:
        - Column renaming (SourceColumn -> DestinationColumn)
        - Data type casting
        - Date/Timestamp formatting
        - Filter by FileId
        """
        try:
            column_mappings = mapping_config.get("columnMapping", [])
            
            for mapping in column_mappings:
                select_columns = mapping.get("selectColumns", [])
                
                for col_map in select_columns:
                    source_col = col_map.get("SourceColumn")
                    dest_col = col_map.get("DestinationColumn")
                    data_type = col_map.get("DataType", "string")
                    source_col_format = col_map.get("SourceColumnFormat", "")
                    column_query = col_map.get("ColumnQuery")
                    
                    # Handle column query (custom SQL-like expressions)
                    if column_query:
                        # For simple cases, evaluate the column query
                        df[dest_col] = df.eval(column_query, engine='python')
                    elif source_col in df.columns:
                        # Rename column
                        if source_col != dest_col:
                            df.rename(columns={source_col: dest_col}, inplace=True)
                        
                        # Apply date/timestamp formatting
                        if data_type == "DateType" and source_col_format:
                            df[dest_col] = pd.to_datetime(df[dest_col], format=source_col_format).dt.date
                        elif data_type == "TimestampType" and source_col_format:
                            df[dest_col] = pd.to_datetime(df[dest_col], format=source_col_format)
                        
                        # Cast data type
                        df[dest_col] = df[dest_col].astype(self._get_pandas_dtype(data_type))
                    else:
                        # Column doesn't exist, create null column
                        df[dest_col] = None
            
            # Filter by FileId
            if "FileID" in df.columns and file_id:
                df = df[df["FileID"] == file_id]
            
            return df
            
        except Exception as e:
            logger.error(f"Error applying mappings: {str(e)}")
            raise
    
    def _custom_select(self, df: pd.DataFrame, required_cols: List[str]) -> pd.DataFrame:
        """Ensure all required columns exist, fill missing with None."""
        for col in required_cols:
            if col not in df.columns:
                df[col] = None
        
        # Keep only required columns in correct order
        return df[required_cols]
    
    def _write_consolidated(self, df: pd.DataFrame, output_path: str):
        """Write consolidated data as parquet."""
        os.makedirs(output_path, exist_ok=True)
        df.to_parquet(f"{output_path}consolidated_data.parquet", append=True)
        logger.info(f"Written to: {output_path}")
    
    def _get_pandas_dtype(self, spark_dtype: str) -> str:
        """Map Spark data types to Pandas dtypes."""
        dtype_map = {
            "StringType": "object",
            "IntegerType": "int64",
            "LongType": "int64",
            "DoubleType": "float64",
            "FloatType": "float32",
            "BooleanType": "bool",
            "DateType": "object",
            "TimestampType": "datetime64[ns]",
            "DecimalType": "float64"
        }
        return dtype_map.get(spark_dtype, "object")