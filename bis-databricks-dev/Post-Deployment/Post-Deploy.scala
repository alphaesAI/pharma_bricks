// Databricks notebook source
// MAGIC %md
// MAGIC #This script is to be used to call Post-Deployment scripts.
// MAGIC 
// MAGIC **This script should not be removed**
// MAGIC 
// MAGIC To use this script, call Notebooks from within a release folder to be executed after a deployment.  The scripts should be setup in a way so that they are only executed when needed.
// MAGIC 
// MAGIC Older scripts should be remove once their release has been completed.

// COMMAND ----------

// DBTITLE 1,Add notebook references below
//%run "./Notebooks/IDAP-2123_UpdateMemberSchema"
