# pythonedi/consolidation/loop_consolidation_files.py
import json
import logging
from typing import List, Dict
from .movefiletoconsolidation import MoveFileToConsolidation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoopConsolidationFiles:
    """
    Orchestrates consolidation by looping through FileIds and calling MoveFileToConsolidation.
    Replaces LoopConsolidationFiles.scala
    """
    
    def __init__(self):
        self.move_consolidation = MoveFileToConsolidation()
        self.results = []
    
    def process(self, consolidation_json: str) -> List[Dict]:
        """
        Parse consolidation JSON and loop through FileIds.
        
        Args:
            consolidation_json: JSON string containing FileIds array
            
        Returns:
            List of results from each consolidation
        """
        try:
            config = json.loads(consolidation_json)
            file_ids = config.get("FileIds", [])
            
            logger.info(f"Processing {len(file_ids)} files for consolidation")
            
            for file_config in file_ids:
                result = self._process_file(file_config)
                self.results.append(result)
            
            return self.results
            
        except Exception as e:
            logger.error(f"Error in consolidation loop: {str(e)}")
            raise
    
    def _process_file(self, file_config: Dict) -> Dict:
        """
        Process single file through consolidation.
        
        Args:
            file_config: Configuration for single file
            
        Returns:
            Result dictionary with status and counts
        """
        try:
            file_id = file_config.get("FileId")
            current_container = file_config.get("CurrentContainer")
            current_folder_path = file_config.get("CurrentFolderPath")
            consolidated_layer_data_model = file_config.get("ConsolidatedLayerDataModel")
            consolidated_layer_data_model_filepath = file_config.get("ConsolidatedLayerDataModelFilePath")
            consolidated_mapping_file_name = file_config.get("ConsolidatedMappingFileName")
            consolidated_mapping_file_path = file_config.get("ConsolidatedMappingFilePath")
            consolidated_folder_path = file_config.get("ConsolidatedFolderPath")
            
            logger.info(f"Processing FileId: {file_id}")
            
            result = self.move_consolidation.process(
                file_id=file_id,
                current_container=current_container,
                current_folder_path=current_folder_path,
                consolidated_layer_data_model=consolidated_layer_data_model,
                consolidated_layer_data_model_filepath=consolidated_layer_data_model_filepath,
                consolidated_mapping_file_name=consolidated_mapping_file_name,
                consolidated_mapping_file_path=consolidated_mapping_file_path,
                consolidated_folder_path=consolidated_folder_path
            )
            
            return {
                "FileID": file_id,
                "DataGroupTrackingID": file_config.get("DataGroupTrackingID"),
                "DataGroupMappingId": file_config.get("DataGroupMappingId"),
                "CurrentContainer": current_container,
                "CurrentFolderPath": current_folder_path,
                "ConsolidatedFolderPath": consolidated_folder_path,
                "CurrentJobId": result.get("CurrentJobId"),
                "ConsolidatedCount": result.get("ConsolidatedCount"),
                "Status": result.get("Status"),
                "ErrorMessage": result.get("ErrorMessage", "")
            }
            
        except Exception as e:
            logger.error(f"Error processing file {file_config.get('FileId')}: {str(e)}")
            return {
                "FileID": file_config.get("FileId"),
                "Status": "FAILED",
                "ConsolidatedCount": 0,
                "ErrorMessage": str(e)
            }