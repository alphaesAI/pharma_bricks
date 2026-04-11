# Databricks notebook source
# MAGIC %md
# MAGIC ##parallel_testing_source_notebook

# COMMAND ----------

# DBTITLE 1,Libraries Required
from datetime import datetime

# COMMAND ----------

# DBTITLE 1,Cell to get location details from ADF pipeline
# # A location variable was created for QSI and Q360 to get values from pipeline and pass as arguments to the notebook

#location variable for Q360 files
member_general_location_q360 = 'empty'       
member_enroll_location_q360  = 'empty'
visit_location_q360 = 'empty'
lab_location_q360 = 'empty'
pharmacy_location_q360 = 'empty'
Provider_location_q360 = 'empty'
mmdf_location_q360 = 'empty' 

  #location variable for QSI files
member_general_location_qsi = 'empty'
member_enroll_location_qsi  = 'empty'
visit_location_qsi = 'empty'
age_in_claim_qsi = 'empty'
emr_claim_qsi = 'empty'
fcf_claim_qsi = 'empty'
lab_location_qsi = "empty"
pharmacy_location_qsi ='empty'

# provider and mmdf has no QSI file 





# COMMAND ----------

# DBTITLE 1,Cell to get location details f
clientName = dbutils.widgets.get('clientname').lower()
# # A location variable was created for QSI and Q360 to get values from pipeline and pass as arguments to the notebook
#location variable for Q360 files
q360_files = dbutils.fs.ls(f"/mnt/{clientName}/Q360/Q360")
qsi_files = (dbutils.fs.ls(f"/mnt/{clientName}/Q360/QSI"))

# loop to get q360 files from container
for q360 in q360_files:
  q360_location = q360.name
  q360_list = q360_location.lower().split('_')
  if('memgen' in q360_list):
    member_general_location_q360 = q360_location    
  elif('memenr' in q360_list):
    member_enroll_location_q360 = q360_location
  elif('visit' in q360_list):
    visit_location_q360 = q360_location
  elif('lab' in q360_list):
    lab_location_q360 = q360_location
  elif('pharmacy' in q360_list):
    pharmacy_location_q360 = q360_location
  elif('provider' in q360_list):
    Provider_location_q360 = q360_location
  elif('mmdf' in q360_list):
    mmdf_location_q360 = q360_location

# loop to get qsi files from container
for qsi in qsi_files:
  qsi_location = qsi.name
  qsi_list = qsi_location.lower().split('_')             
  if('member' in qsi_list):
    member_general_location_qsi = qsi_location    
  elif('memberenroll' in qsi_list): 
    member_enroll_location_qsi  = qsi_location
  elif('vision' in qsi_list):
    visit_location_qsi = qsi_location
  elif('fcf' in qsi_list):
    fcf_claim_qsi = qsi_location
  elif(('emr' in qsi_list) and ('claims' in qsi_list)):
    emr_claim_qsi = qsi_location
  elif('agein' in qsi_list):
    age_in_claim_qsi = qsi_location
  elif(('lab' in qsi_list) and ('claims' in qsi_list)):
    lab_location_qsi = qsi_location
  elif('pharmacy' in qsi_list):
    pharmacy_location_qsi = qsi_location




# creating QSI_Converted and Results directory inside container to store respective results
dbutils.fs.mkdirs(f"/mnt/{clientName}/Q360/QSI_Converted")
folder_time = datetime.now().strftime("%Y-%m-%d")
dbutils.fs.mkdirs(f"/mnt/{clientName}/Q360/Results/{folder_time}")


# COMMAND ----------

# DBTITLE 1,QSI Transformation activation script
# Timeout  --> set to 1000 secounds depends on the file size
# Exception is added in order to reduce the dependency of a single notebook run
try:
  member_notebook_status = dbutils.notebook.run('./1_Basic_Transform_General_Membership',1000, \
    arguments={"clientname":clientName,"location":member_general_location_q360,"location2":member_general_location_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_General_Membership script run is {member_notebook_status}')
except Exception as Error:
  print("Basic_Transform_General_Membership - No Files in either QSI or Q360")


try:
  member_enroll_notebook_status = dbutils.notebook.run('./2_Basic_Transform_Membership_Enrollment',1000 ,\
    arguments={"clientname":clientName,"location":member_enroll_location_q360,"location2":member_enroll_location_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_Membership_Enrollment script run is {member_enroll_notebook_status}')

except Exception as Error:
  print("No Files in either QSI or Q360")


try:
  visit_notebook_status = dbutils.notebook.run('./3_Basic_Transform_Visit',1000,\
    arguments={"clientname":clientName,"location":visit_location_q360,"location2":visit_location_qsi,
                "location3":age_in_claim_qsi,"location4":emr_claim_qsi,"location5":fcf_claim_qsi,"destination_location":folder_time})    
  print(f'Basic_Transform_Visit script run is {visit_notebook_status}')                                                     
except Exception as Error:
  print("Basic_Transform_Visit -No Files in either QSI or Q360")


try:
  lab_notebook_status = dbutils.notebook.run('./4_Basic_Transform_Lab',1000,\
    arguments={"clientname":clientName,"location":lab_location_q360,"location2":lab_location_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_Lab script run is {lab_notebook_status}')
except Exception as Error:
  print("Basic_Transform_Lab' - No Files in either QSI or Q360")

  
    
try:
  pharmacy_notebook_status = dbutils.notebook.run('./5_Basic_Transform_Pharmacy',1000,\
    arguments={"clientname":clientName,"location":pharmacy_location_q360,"location2":pharmacy_location_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_Pharmacy script run is {pharmacy_notebook_status}')
except Exception as Error:
  print("Basic_Transform_Pharmacy-No Files in either QSI or Q360")

  

try:
  provider_notebook_status = dbutils.notebook.run('./6_Basic_Transform_Provider',1000,\
    arguments={"clientname":clientName,"location":Provider_location_q360,"location2":pharmacy_location_qsi,"location3":visit_location_qsi,
                "location4":age_in_claim_qsi,"location5":emr_claim_qsi,"location6":fcf_claim_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_Provider-Basic_Transform_Provider script is {provider_notebook_status}')
except Exception as Error:
  print("Basic_Transform_Provider -No Files in either QSI or Q360")

try:
  MMDF_notebook_status = dbutils.notebook.run('./7_Basic_Transform_MMDF',1000,\
    arguments={"clientname":clientName,"location":mmdf_location_q360,
                "location2":member_general_location_qsi,"location3":member_enroll_location_qsi,"destination_location":folder_time})
  print(f'Basic_Transform_MMDF script run completed is {MMDF_notebook_status}')
except Exception as Error:
  print("Basic_Transform_MMDF-No Files in either QSI or Q360")

  

