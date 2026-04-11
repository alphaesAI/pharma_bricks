/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm
PROD - bcbsks, bcbsm
*/
CREATE TABLE [devidap1].[HICN_MBI_CrossWalk] 
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,	
	Contract  varchar(5) NULL,
	PBP varchar(3) NULL,
	HICN varchar(12) NULL,
	MBI varchar(11) NULL,
	Surname varchar(30) NULL,
	FirstName varchar(12) NULL,
	DateOfBirth integer NULL,
	DateOfDeath integer NULL,
	Gender varchar(1) NULL,
	RecentEnrollmentDate integer NULL,
	RecentDisenrollmentDate integer NULL
)