DECLARE @GCPostCount INTEGER = 0

IF EXISTS(SELECT 0 
			FROM INFORMATION_SCHEMA.TABLES 
			WHERE TABLE_SCHEMA = 'devidap1' 
			AND TABLE_NAME = 'GoldenClaim_Temp')
BEGIN
	--remove old records from gch
	TRUNCATE TABLE devidap1.GoldenClaim
	--Check for data 
	SELECT @GCPostCount = COUNT(1) FROM devidap1.GoldenClaim_Temp

	IF (@GCPostCount > 0)
	BEGIN
		PRINT('Reloading GCH and dropping temp')
	--Load GCH
		INSERT INTO devidap1.GoldenClaim
		SELECT	CAST(GeneratedGoldenClaimsUniqueKey AS VARCHAR(255)) AS GeneratedGoldenClaimsUniqueKey, 
				CAST(GeneratedMedicalClaimsUniqueKey AS VARCHAR(255))  AS GeneratedMedicalClaimsUniqueKey,
				CAST(ClientID AS VARCHAR(20))  AS ClientID, 
				CAST(FileLayoutID AS INT)  AS FileLayoutID, 
				CAST(FileLayoutDescription AS VARCHAR(255))  AS FileLayoutDescription, 
				CAST(ClaimNumber AS VARCHAR(20))  AS ClaimNumber, 
				CAST(OriginalClaimNumber AS VARCHAR(20))  AS OriginalClaimNumber, 
				CAST(BeneficiaryID AS VARCHAR(12))  AS BeneficiaryID, 
				CAST(PlanMemberID AS VARCHAR(30))  AS PlanMemberID, 
				CAST(CMSContractNumber AS VARCHAR(6))  AS CMSContractNumber, 
				CAST(BillTypeCode AS VARCHAR(5))  AS BillTypeCode, 
				CAST(ClaimTypeInd AS VARCHAR(1)) AS ClaimTypeInd, 
				CAST(ClaimWeight AS BIGINT)  AS ClaimWeight, 
				CAST(ClaimStatus AS VARCHAR(1))  AS ClaimStatus, 
				CAST(ClaimProcessDate AS Datetime2(7))  AS ClaimProcessDate, 
				CAST(ClaimSource AS VARCHAR(20))  AS ClaimSource, 
				CAST(LoadTimestamp AS Datetime2(7)) AS LoadTimestamp
		FROM devidap1.GoldenClaim_Temp

		DROP TABLE devidap1.GoldenClaim_Temp
	END

END