CREATE TABLE #clientCode.consolidated_ma_appointmentTypeDesc (
 ClientID string
,LoadDateTime date
,FileID bigint
,FileLayoutID int
,FileLayoutDescription string
,Client string
,Market string
,Metric string
,AppointmentTypeDesc string
,AppointmentTypeDesc_USE string
,CountFlag string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/AppointmentTypeDesc'