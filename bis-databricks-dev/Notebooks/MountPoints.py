# Databricks notebook source
# DBTITLE 1,Deployment Variables
#####ClientNames per environment
#dev - devidap
#qa - qaidap
#stage - BCBSKS
#prod - BCBSKS


#####DEV NOTE
# When checking into source control replace the below variables with the following
# remove the "/" in the 'Name' (Nam/e).  This was done so the deployment process doesn't replace the deployment variable.  :)
#client1Name = 'CHANGE_FOR_DEPLOYMENT_client1Nam/e'
#datalakeName = 'CHANGE_FOR_DEPLOYMENT_datalakeNam/e'
#blobName = 'CHANGE_FOR_DEPLOYMENT_blobNam/e'
#exportName = 'CHANGE_FOR_DEPLOYMENT_exportNam/e'

client1Name = 'CHANGE_FOR_DEPLOYMENT_client1Name'.lower()
datalakeName = 'CHANGE_FOR_DEPLOYMENT_datalakeName'
blobName = 'CHANGE_FOR_DEPLOYMENT_blobName'
exportName = 'CHANGE_FOR_DEPLOYMENT_exportName'

datalakeKey = dbutils.secrets.get(scope = "idapkeyvault", key = "datalakestorage")
blobKey = dbutils.secrets.get(scope = "idapkeyvault", key = "blobstorage")
exportKey = dbutils.secrets.get(scope = "idapkeyvault", key = "datalakestorage04")

# COMMAND ----------

dlMP = "/mnt/export" +clientName

if any(mount.mountPoint == dlMP for mount in dbutils.fs.mounts()) : print("Mount Point: '"+dlMP+"' Exists")
else : 
    dbutils.fs.mount(
      source = "wasbs://"+clientName+"@" + extractName + ".blob.core.windows.net",
      mount_point = dlMP,
      extra_configs = {"fs.azure.account.key." + extractName+ ".blob.core.windows.net" : extractKey }
    )
    print("Mount Point: '"+dlMP+"' Created")

# COMMAND ----------

# DBTITLE 1,Client Datalake
dlMP = "/mnt/" +client1Name

if any(mount.mountPoint == dlMP for mount in dbutils.fs.mounts()) : print("Mount Point: '"+dlMP+"' Exists")
else : 
    dbutils.fs.mount(
      source = "wasbs://"+client1Name+"@" + datalakeName + ".blob.core.windows.net",
      mount_point = dlMP,
      extra_configs = {"fs.azure.account.key." + datalakeName+ ".blob.core.windows.net" : datalakeKey }
    )
    print("Mount Point: '"+dlMP+"' Created")

# COMMAND ----------

# DBTITLE 1,Fileconfig
fcMP = "/mnt/fileconfig"

if any(mount.mountPoint == fcMP for mount in dbutils.fs.mounts()) : print("Mount Point: '"+fcMP+"' Exists")
else : 
    dbutils.fs.mount(
      source = "wasbs://fileconfig@" + datalakeName + ".blob.core.windows.net",
      mount_point = fcMP,
      extra_configs = {"fs.azure.account.key." + datalakeName + ".blob.core.windows.net" : datalakeKey }
    )
    print("Mount Point: '"+fcMP+"' Created")

# COMMAND ----------

# DBTITLE 1,Client SourceBlob
bMP = "/mnt/" + client1Name + "blob"

if any(mount.mountPoint == bMP for mount in dbutils.fs.mounts()) : print("Mount Point: '"+bMP+"' Exists")
else : 
    dbutils.fs.mount(
      source = "wasbs://"+client1Name+"@" + blobName + ".blob.core.windows.net",
      mount_point = bMP,
      extra_configs = {"fs.azure.account.key." + blobName + ".blob.core.windows.net" : blobKey }
    )
    print("Mount Point: '"+bMP+"' Created")
