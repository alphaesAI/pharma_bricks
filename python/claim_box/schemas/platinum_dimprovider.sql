-- BIS-Style Dimension Provider Table (PostgreSQL)
-- SCD Type 2 support with effective dates

CREATE TABLE IF NOT EXISTS platinum_dimprovider (
    providerKey SERIAL PRIMARY KEY,
    providerID VARCHAR(100) NULL,
    effectiveStartDate DATE NOT NULL DEFAULT CURRENT_DATE,
    effectiveEndDate DATE NULL,
    isCurrent BOOLEAN NOT NULL DEFAULT TRUE,
    npi VARCHAR(50) NOT NULL,
    tin VARCHAR(50) NULL,
    lastName VARCHAR(300) NULL,
    firstName VARCHAR(300) NULL,
    middleName VARCHAR(100) NULL,
    phoneNumber VARCHAR(60) NULL,
    address1 VARCHAR(510) NULL,
    address2 VARCHAR(510) NULL,
    city VARCHAR(200) NULL,
    state VARCHAR(4) NULL,
    zipCode VARCHAR(20) NULL,
    practiceCode VARCHAR(100) NULL,
    practiceName VARCHAR(510) NULL,
    providerOrgCode VARCHAR(100) NULL,
    providerOrgName VARCHAR(510) NULL,
    providerSpecialtyDescription VARCHAR(200) NULL,
    taxonomyCode1 VARCHAR(20) NULL,
    hpSpecialtyCode1 VARCHAR(4) NULL,
    advProviderSpecialtyCode1 VARCHAR(20) NULL,
    taxonomyCode2 VARCHAR(20) NULL,
    hpSpecialtyCode2 VARCHAR(4) NULL,
    advProviderSpecialtyCode2 VARCHAR(20) NULL,
    taxonomyCode3 VARCHAR(20) NULL,
    hpSpecialtyCode3 VARCHAR(4) NULL,
    advProviderSpecialtyCode3 VARCHAR(20) NULL,
    taxonomyCode4 VARCHAR(20) NULL,
    hpSpecialtyCode4 VARCHAR(4) NULL,
    advProviderSpecialtyCode4 VARCHAR(20) NULL,
    taxonomyCode5 VARCHAR(20) NULL,
    hpSpecialtyCode5 VARCHAR(4) NULL,
    advProviderSpecialtyCode5 VARCHAR(20) NULL,
    isPrescribePrivilege VARCHAR(20) NULL,
    providerDEA VARCHAR(50) NULL,
    payerID VARCHAR(50) NULL,
    isContracted VARCHAR(20) NULL,
    providerHAI VARCHAR(20) NULL,
    hospitalID VARCHAR(200) NULL,
    isExcludedFromProviderReporting VARCHAR(20) NULL,
    altProvReporting1 VARCHAR(300) NULL,
    altProvReporting2 VARCHAR(300) NULL,
    altProvReporting3 VARCHAR(300) NULL,
    altProvReporting4 VARCHAR(300) NULL,
    altProvReporting5 VARCHAR(300) NULL,
    altProvReporting6 VARCHAR(300) NULL,
    altProvReporting7 VARCHAR(300) NULL,
    altProvReporting8 VARCHAR(300) NULL,
    altProvReporting9 VARCHAR(300) NULL,
    altProvReporting10 VARCHAR(300) NULL,
    programType VARCHAR(200) NULL,
    practiceTargetedStatus VARCHAR(200) NULL,
    ProductID VARCHAR(100) NULL,
    ProviderType VARCHAR(100) NULL,
    createdDateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedDateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fullRowHash VARCHAR(64) NULL,
    
    -- Unique constraint for SCD2
    CONSTRAINT uq_provider_natural_key UNIQUE (npi, isCurrent, effectiveStartDate)
);

-- Indexes for performance
CREATE INDEX idx_dimprovider_npi ON platinum_dimprovider(npi);
CREATE INDEX idx_dimprovider_iscurrent ON platinum_dimprovider(isCurrent);
CREATE INDEX idx_dimprovider_providerid ON platinum_dimprovider(providerID);

-- Comments for documentation
COMMENT ON TABLE platinum_dimprovider IS 'Provider dimension table (SCD Type 2) - stores historical provider attributes';
COMMENT ON COLUMN platinum_dimprovider.providerKey IS 'Surrogate key (auto-generated)';
COMMENT ON COLUMN platinum_dimprovider.npi IS 'National Provider Identifier (natural key)';
COMMENT ON COLUMN platinum_dimprovider.isCurrent IS 'SCD Type 2 flag: TRUE = current record, FALSE = historical';
