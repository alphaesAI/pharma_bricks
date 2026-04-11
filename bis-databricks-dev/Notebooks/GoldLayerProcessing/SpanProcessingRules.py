# Databricks notebook source
def SpanProcessingRules(dfSourceFile):
  
  dfSourceFile.createOrReplaceTempView("SourceTable")
  
  df = spark.sql("""
	WITH source AS (
        SELECT *
        FROM SourceTable
        )
        
	,toVoid AS (
      SELECT BISInternalPersonID, UniquePersonKey, StartDate, EndDate, FileID, EndDateEoY
      FROM source
      WHERE EndDate <= StartDate
      )
      
    ,errors AS (
        SELECT *
              ,case when (FileLayoutDescription= 'MEMOUT' AND StartDate = EndDate) OR
                       ((StartDate <= EndDate) AND
                        (StartDate BETWEEN (max(StartDate) 
                            OVER(PARTITION BY FileId,BISInternalPersonID,CMSContractNumber,FileLayoutID ORDER BY StartDate, EndDate DESC rows BETWEEN unbounded preceding AND 1 preceding))
                                    AND (max(EndDate) 
                            OVER(PARTITION BY FileId,BISInternalPersonID,CMSContractNumber,FileLayoutID ORDER BY StartDate, EndDate DESC rows BETWEEN unbounded preceding AND 1 preceding))
                        ))
                  THEN 'error' END AS Error_Flag
        FROM source
        )
        
	,nonErrors AS (
        SELECT *
              ,CASE WHEN rownum = 1 THEN 1 ELSE 0 END Recent
        FROM (
            SELECT *
                ,row_number() OVER(PARTITION BY BISInternalPersonID,CMSContractNumber,FileLayoutID,StartDate ORDER BY FileId DESC, EndDate) AS rownum
            FROM errors
            WHERE Error_Flag IS null
            )a
        )

	,voided AS (
        SELECT s.*
            ,CASE WHEN v.BISInternalPersonID IS NOT NULL THEN 'void' END AS Void_Flag
        FROM nonErrors s
          LEFT JOIN toVoid v ON s.BISInternalPersonID = v.BISInternalPersonID 
                        AND s.StartDate = v.StartDate
                        AND s.FileID <= v.FileID
        )
    
    ,active AS (
        SELECT old.*
             ,CASE WHEN old.Recent = 1 AND new.BISInternalPersonID IS NOT null THEN 'inactive' 
                   WHEN old.Recent = 0 AND Void_Flag IS NULL THEN 'inactive' 
                   ELSE null END Inactive_Flag
        FROM voided old
            LEFT JOIN (SELECT BISInternalPersonID, StartDate, Recent  
                       FROM voided
                       WHERE Recent = 1) new ON old.BISInternalPersonID = new.BISInternalPersonID
                                 AND (new.StartDate > old.StartDate AND new.StartDate < old.EndDateEoY) 
        )

    SELECT * 
    FROM active
    UNION
    SELECT *
        ,null as Inactive_Flag
    FROM voided
    WHERE Void_Flag IS NOT NULL
    UNION
    SELECT *
        ,-1 as rownum
        ,null as Recent
        ,null as Void_Flag
        ,null as Inactive_Flag
    FROM errors 
    WHERE Error_Flag IS NOT NULL
	""")
  return df

# COMMAND ----------

# MAGIC %md
# MAGIC Specification  
# MAGIC 1.	Each Member Span record has StartDate and EndDate, if EndDate is not populated, it will be treated as 12/31/9999. 
# MAGIC 2.	StartDate and EndDate is for the Span period for all values on the record line (including Product Benefit flags), not just member eligibility for EFF span type. 
# MAGIC 3.	The granularity of StartDate and EndDate for a member can be monthly, but neither necessary nor recommended (for performance reasons) unless the member's eligibility changes month over month. 
# MAGIC 4.	For each member (based on MemberID, PlanID), once the StartDate is communicated, it remains valid unless specifically voided. 
# MAGIC 	a.	To void a StartDate for a member, a record with the same StartDate but an EndDate earlier than StartDate should be sent for processing. 
# MAGIC 	b.	A member's eligibility span can be shortened or expanded in a subsequent communication by sending the same StartDate, but a different EndDate.  
# MAGIC 	c.	For all member span records in the same file, void records will be processed first before other records. 
# MAGIC 5.	For member's span records communicated to Advantature in different months with the same StartDate, the record currently processed trumps the records processed earlier.
# MAGIC 6.	There should be no overlapping span records for the same member in the same file. If received, the last record inserted into Adventure system will be processed and other records will be flagged for error. 
# MAGIC 	a.	Also Error flag records from MEMOUT where Startdate=Enddate
# MAGIC 	b.	Historical spans overlapping with span records from current file will be marked as inactive. The latest loaded span record (from current file) will be marked as active.
# MAGIC 7.	If there is a span record with high end date AND also there is a second span with start date greater than first span start date, then first span will be ended with one day less than second span start date. 
# MAGIC For example, For all members with the Span record start date 1/1/2013 and end date 12/31/999, when we receive a second span record with start date 1/1/2014, the first span end date should be updated to 12/31/2013.
