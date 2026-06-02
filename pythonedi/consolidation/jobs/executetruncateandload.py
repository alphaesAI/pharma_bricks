# pythonedi/consolidation/execute_truncate_and_load.py
import psycopg2
import pandas as pd
import logging
from typing import Dict
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExecuteTruncateAndLoad:
    """
    Load consolidated Delta/Parquet data to PostgreSQL.
    Replaces ExecuteTruncateAndLoad.scala (Azure Synapse) with PostgreSQL support.
    """
    
    def __init__(self, 
                 pg_host: str,
                 pg_database: str,
                 pg_user: str,
                 pg_password: str,
                 pg_port: int = 5432):
        """
        Initialize PostgreSQL connection parameters.
        
        Args:
            pg_host: PostgreSQL host
            pg_database: Database name
            pg_user: Database user
            pg_password: Database password
            pg_port: PostgreSQL port (default 5432)
        """
        self.pg_host = pg_host
        self.pg_database = pg_database
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.pg_port = pg_port
        self.connection = None
        self.job_id = str(datetime.now().timestamp())
    
    def process(self,
                consolidated_path: str,
                dest_table: str) -> Dict:
        """
        Truncate target table and load consolidated data.
        
        Args:
            consolidated_path: Path to consolidated parquet/delta
            dest_table: Target PostgreSQL table name
            
        Returns:
            Result dictionary with status
        """
        result = {
            "CurrentJobId": self.job_id,
            "Status": "SUCCESS",
            "ErrorMessage": ""
        }
        
        try:
            # Connect to PostgreSQL
            self.connection = psycopg2.connect(
                host=self.pg_host,
                database=self.pg_database,
                user=self.pg_user,
                password=self.pg_password,
                port=self.pg_port
            )
            
            cursor = self.connection.cursor()
            
            logger.info(f"Connected to PostgreSQL: {self.pg_host}/{self.pg_database}")
            
            # Read consolidated data
            df = pd.read_parquet(consolidated_path)
            logger.info(f"Read {len(df)} rows from consolidated path")
            
            # Get target table schema
            cursor.execute(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (dest_table,))
            
            target_schema = {row[0]: row[1] for row in cursor.fetchall()}
            logger.info(f"Target table '{dest_table}' has {len(target_schema)} columns")
            
            # Ensure all required columns exist in DataFrame
            df_final = self._prepare_dataframe(df, target_schema)
            
            # Replace empty strings with None
            df_final = df_final.replace('', None)
            
            # Truncate target table
            cursor.execute(f"TRUNCATE TABLE {dest_table} CASCADE;")
            logger.info(f"Truncated table: {dest_table}")
            
            # Insert data into PostgreSQL
            self._insert_dataframe(cursor, df_final, dest_table, target_schema)
            
            self.connection.commit()
            logger.info(f"Successfully loaded {len(df_final)} rows into {dest_table}")
            
            result["Status"] = "SUCCESS"
            
        except Exception as e:
            if self.connection:
                self.connection.rollback()
            logger.error(f"Error in truncate and load: {str(e)}")
            result["Status"] = f"FAILURE: {str(e)}"
            result["ErrorMessage"] = str(e)
        
        finally:
            if self.connection:
                self.connection.close()
                logger.info("PostgreSQL connection closed")
        
        return result
    
    def _prepare_dataframe(self, df: pd.DataFrame, target_schema: Dict) -> pd.DataFrame:
        """
        Prepare DataFrame to match target schema.
        Add missing columns as None.
        """
        for col_name in target_schema.keys():
            if col_name not in df.columns:
                df[col_name] = None
        
        # Keep only columns in target schema, in correct order
        df = df[[col for col in target_schema.keys() if col in df.columns]]
        
        return df
    
    def _insert_dataframe(self, 
                          cursor,
                          df: pd.DataFrame,
                          table_name: str,
                          target_schema: Dict):
        """
        Insert DataFrame into PostgreSQL table.
        """
        try:
            # Get column names and create placeholder string
            columns = list(df.columns)
            placeholders = ','.join(['%s'] * len(columns))
            col_names = ','.join([f'"{col}"' for col in columns])
            
            insert_query = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"
            
            # Convert DataFrame rows to list of tuples
            rows = [tuple(row) for row in df.values]
            
            # Insert in batches (1000 rows at a time)
            batch_size = 1000
            for i in range(0, len(rows), batch_size):
                batch = rows[i:i + batch_size]
                cursor.executemany(insert_query, batch)
                logger.info(f"Inserted batch {i // batch_size + 1}/{(len(rows) + batch_size - 1) // batch_size}")
            
        except Exception as e:
            logger.error(f"Error inserting data: {str(e)}")
            raise