CREATE TABLE [devidap1].[gold_ma_membergroup]
( 
     [SubscriberID]  nvarchar(100) NULL
    ,[BeneficiaryID]  nvarchar(100) NULL
    ,[StartDate]  date
    ,[EndDate]  date 
    ,[CMSContractNumber]  nvarchar(100) NULL
    ,[GroupNumber]  nvarchar(100) NULL
    ,[GroupSuffix]  nvarchar(100) NULL
    ,[SourceFileID]  bigint NULL
    ,[LoadDateTime]	datetime2(7) NULL
) 