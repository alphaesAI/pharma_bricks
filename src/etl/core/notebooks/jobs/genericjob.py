# pythonedi/consolidation/generic_member_job.py
import json
import logging
from typing import Dict
from .executetruncateandload import ExecuteTruncateAndLoad

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GenericMemberJob:
    """
    Orchestrates consolidated Member data loading to PostgreSQL.
    Replaces GenericSynapseJob.scala for Member table.
    """
    
    def __init__(self,
                 pg_host: str,
                 pg_database: str,
                 pg_user: str,
                 pg_password: str):
        """
        Initialize with PostgreSQL connection details.
        """
        self.pg_host = pg_host
        self.pg_database = pg_database
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.etl_loader = ExecuteTruncateAndLoad(
            pg_host=pg_host,
            pg_database=pg_database,
            pg_user=pg_user,
            pg_password=pg_password
        )
    
    def process(self,
                client_container: str,
                synapse_table_name: str,
                consolidated_folder_path: str) -> Dict:
        """
        Load consolidated Member data to PostgreSQL.
        
        Args:
            client_container: Client container/code
            synapse_table_name: Target table name (e.g., 'Member')
            consolidated_folder_path: Path to consolidated Member data
            
        Returns:
            Result dictionary with status and job info
        """
        result = {
            "CurrentJobId": self.etl_loader.job_id,
            "Status": "SUCCESS",
            "ErrorMessage": ""
        }
        
        try:
            # Build destination table name
            dest_table = f"{client_container}.{synapse_table_name}"
            
            # Build consolidated path
            mount_point = "/mnt/"
            consolidated_path = f"{mount_point}{client_container}{consolidated_folder_path}"
            
            logger.info(f"Processing Member table: {dest_table}")
            logger.info(f"Source path: {consolidated_path}")
            
            # Execute truncate and load
            load_result = self.etl_loader.process(
                consolidated_path=consolidated_path,
                dest_table=dest_table
            )
            
            result.update(load_result)
            
        except Exception as e:
            logger.error(f"Error in Member job: {str(e)}")
            result["Status"] = "FAILURE"
            result["ErrorMessage"] = str(e)
        
        return result
    
    def process_from_config(self, config_json: str) -> Dict:
        """
        Process using configuration JSON.
        
        Args:
            config_json: JSON string with parameters
            
        Returns:
            Result dictionary
        """
        try:
            config = json.loads(config_json)
            
            return self.process(
                client_container=config.get("ClientContainer"),
                synapse_table_name=config.get("SynapseTableName"),
                consolidated_folder_path=config.get("ConsolidatedFolderPath")
            )
            
        except Exception as e:
            logger.error(f"Error parsing config: {str(e)}")
            return {
                "Status": "FAILURE",
                "ErrorMessage": str(e)
            }