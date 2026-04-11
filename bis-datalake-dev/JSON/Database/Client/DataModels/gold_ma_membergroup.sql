CREATE TABLE #clientCode.gold_ma_membergroup (
    SubscriberID  string
    ,BeneficiaryID  string
    ,CMSContractNumber  string
    ,GroupNumber  string
    ,GroupSuffix  string
    ,StartDate  date
    ,EndDate  date
    ,SourceFileID  bigint
    ,LoadDateTime  timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Client/MemberGroup'