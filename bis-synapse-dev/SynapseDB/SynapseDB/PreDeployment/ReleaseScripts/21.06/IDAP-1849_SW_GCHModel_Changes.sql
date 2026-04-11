DECLARE @GCHCount INTEGER = 0

IF EXISTS(SELECT 0 
			FROM INFORMATION_SCHEMA.TABLES 
			WHERE TABLE_SCHEMA = 'devidap1' 
			AND TABLE_NAME = 'tmp_ms_xx_GoldenClaimHistory')
BEGIN
DROP TABLE devidap1.tmp_ms_xx_GoldenClaimHistory
END

IF EXISTS(SELECT 1 FROM sys.columns 
          WHERE Name = N'IsDMEClaim'
          AND Object_ID = Object_ID(N'devidap1.GoldenClaimHistory'))
BEGIN
	PRINT 'Old Structure Found For GoldenClaim.  Beginning Update'

	--Check for data 
	SELECT @GCHCount = COUNT(1) FROM devidap1.GoldenClaimHistory

	PRINT 'Checking for counts of older data'
	IF (@GCHCount > 0)
	BEGIN

		--CREATE TEMP TABLE TO HOLD CURRENT TABLE DATA.  THIS IS FOR THE DEPLOYMENT.
		IF NOT EXISTS (SELECT 0 
				   FROM INFORMATION_SCHEMA.TABLES 
				   WHERE TABLE_SCHEMA = 'devidap1' 
				   AND TABLE_NAME = 'GoldenClaimHistory_Temp')
		BEGIN
			CREATE TABLE devidap1.GoldenClaimHistory_Temp	
			(
				GeneratedGoldenClaimsUniqueKey varchar(255) NOT NULL PRIMARY KEY NONCLUSTERED(GeneratedGoldenClaimsUniqueKey ASC) NOT ENFORCED,
				GeneratedMedicalClaimsUniqueKey varchar(255) NOT NULL , 
				ClientID           varchar(20)  NOT NULL,
				FileLayoutID       int  NOT NULL,
				FileLayoutDescription varchar(255)  NOT NULL,
				ClaimNumber        varchar(20)  NOT NULL,
				OriginalClaimNumber varchar(20)  NULL,
				BeneficiaryID                varchar(12)  NULL,
				PlanMemberID           varchar(30)  NULL,
				CMSContractNumber  varchar(6)  NULL,
				BillTypeCode       varchar(5)  NULL,
				ClaimTypeInd varchar(1)  NULL,
				ClaimWeight        bigint  NOT NULL ,
				ClaimStatus        varchar(1)  NULL,
				ClaimProcessDate   Datetime2(7)  NULL,
				ClaimSource        varchar(20)  NULL, 
				LoadTimestamp   Datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00'
			)
		END

		TRUNCATE TABLE devidap1.GoldenClaimHistory_Temp

		INSERT INTO devidap1.GoldenClaimHistory_Temp
		SELECT	CAST(GeneratedGoldenClaimsUniqueKey AS VARCHAR(250)) AS GeneratedGoldenClaimsUniqueKey, 
				CAST(GeneratedClaimsUniqueKey AS VARCHAR(250))  AS GeneratedMedicalClaimsUniqueKey,
				CAST(ClientID AS VARCHAR(250))  AS ClientID, 
				CAST(FileLayoutID AS INTEGER)  AS FileLayoutID, 
				CAST(FileLayoutDescription AS VARCHAR(250))  AS FileLayoutDescription, 
				CAST(ClaimNum AS VARCHAR(250))  AS ClaimNumber, 
				CAST(OriginalClaimNum AS VARCHAR(250))  AS OriginalClaimNumber, 
				CAST(MBI AS VARCHAR(250))  AS BeneficiaryID, 
				CAST(MemberID AS VARCHAR(250))  AS PlanMemberID, 
				CAST(CMSContractNum AS VARCHAR(250))  AS CMSContractNumber, 
				CAST(BillTypeCode AS VARCHAR(250))  AS BillTypeCode, 
				CAST(ClaimTypeIndicator AS VARCHAR(250)) AS ClaimTypeInd, 
				CAST(ClaimWeight AS BIGINT)  AS ClaimWeight, 
				CAST(ClaimStatus AS VARCHAR(250))  AS ClaimStatus, 
				CAST(ClaimUpdatedDate AS DATETIME)  AS ClaimProcessDate, 
				CAST(ClaimSource AS VARCHAR(250))  AS ClaimSource, 
				CAST(UpdatedTimestamp AS DATETIME) AS LoadTimestamp
		FROM devidap1.GoldenClaimHistory
	END

/*	--Reset the GCH table by dropping and recreating
	DROP TABLE devidap1.GoldenClaimHistory

	CREATE TABLE devidap1.GoldenClaimHistory	
	(
		GeneratedGoldenClaimsUniqueKey varchar(255) NOT NULL  PRIMARY KEY NONCLUSTERED(GeneratedGoldenClaimsUniqueKey ASC) NOT ENFORCED,
		GeneratedMedicalClaimsUniqueKey varchar(255) NOT NULL , 
		ClientID           varchar(20)  NOT NULL,
		FileLayoutID       int  NOT NULL,
		FileLayoutDescription varchar(255)  NOT NULL,
		ClaimNumber        varchar(20)  NOT NULL,
		OriginalClaimNumber varchar(20)  NULL,
		BeneficiaryID                varchar(12)  NULL,
		PlanMemberID           varchar(30)  NULL,
		CMSContractNumber  varchar(6)  NULL,
		BillTypeCode       varchar(5)  NULL,
		ClaimTypeInd varchar(1)  NULL,
		ClaimWeight        bigint  NOT NULL ,
		ClaimStatus        varchar(1)  NULL,
		ClaimProcessDate   Datetime2(7)  NULL,
		ClaimSource        varchar(20)  NULL, 
		LoadTimestamp   Datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00'
	)

	IF (@GCHCount > 0)
	BEGIN
		PRINT('Reloading GCH and dropping temp')
	--Load GCH
		INSERT INTO devidap1.GoldenClaimHistory
		SELECT	CAST(GeneratedGoldenClaimsUniqueKey AS VARCHAR(250)) AS GeneratedGoldenClaimsUniqueKey, 
				CAST(GeneratedMedicalClaimsUniqueKey AS VARCHAR(250))  AS GeneratedMedicalClaimsUniqueKey,
				CAST(ClientID AS VARCHAR(250))  AS ClientID, 
				CAST(FileLayoutID AS INTEGER)  AS FileLayoutID, 
				CAST(FileLayoutDescription AS VARCHAR(250))  AS FileLayoutDescription, 
				CAST(ClaimNumber AS VARCHAR(250))  AS ClaimNumber, 
				CAST(OriginalClaimNumber AS VARCHAR(250))  AS OriginalClaimNumber, 
				CAST(BeneficiaryID AS VARCHAR(250))  AS BeneficiaryID, 
				CAST(PlanMemberID AS VARCHAR(250))  AS PlanMemberID, 
				CAST(CMSContractNumber AS VARCHAR(250))  AS CMSContractNumber, 
				CAST(BillTypeCode AS VARCHAR(250))  AS BillTypeCode, 
				CAST(ClaimTypeInd AS VARCHAR(250)) AS ClaimTypeInd, 
				CAST(ClaimWeight AS BIGINT)  AS ClaimWeight, 
				CAST(ClaimStatus AS VARCHAR(250))  AS ClaimStatus, 
				CAST(ClaimProcessDate AS DATETIME)  AS ClaimProcessDate, 
				CAST(ClaimSource AS VARCHAR(250))  AS ClaimSource, 
				CAST(LoadTimestamp AS DATETIME) AS LoadTimestamp
		FROM devidap1.GoldenClaimHistory_Temp

		DROP TABLE devidap1.GoldenClaimHistory_Temp
	END
*/
END