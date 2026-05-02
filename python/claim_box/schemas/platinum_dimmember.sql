-- BIS-Style Dimension Member Table (PostgreSQL)
-- SCD Type 2 support with effective dates

CREATE TABLE IF NOT EXISTS platinum_dimmember (
    memberKey SERIAL PRIMARY KEY,
    BISInternalPersonID VARCHAR(30) NULL,
    uniquePersonKey VARCHAR(20) NULL,
    planMemberID VARCHAR(20) NOT NULL,
    subscriberID VARCHAR(20) NULL,
    beneficiaryID VARCHAR(30) NULL,
    lastName VARCHAR(300) NULL,
    firstName VARCHAR(300) NULL,
    middleInitial VARCHAR(255) NULL,
    enrolleeUniqueID VARCHAR(50) NULL,
    dateofBirth DATE NULL,
    deceasedDate VARCHAR(20) NULL,
    gender VARCHAR(10) NULL,
    permanentAddressLine1 VARCHAR(600) NULL,
    permanentAddressLine2 VARCHAR(600) NULL,
    permanentCity VARCHAR(100) NULL,
    permanentCounty VARCHAR(20) NULL,
    permanentState VARCHAR(20) NULL,
    permanentZipCode VARCHAR(20) NULL,
    mailingAddressLine1 VARCHAR(600) NULL,
    mailingAddressLine2 VARCHAR(600) NULL,
    mailingCity VARCHAR(100) NULL,
    mailingState VARCHAR(20) NULL,
    mailingZipCode VARCHAR(20) NULL,
    mailingCounty VARCHAR(20) NULL,
    phoneNumber VARCHAR(20) NULL,
    email VARCHAR(255) NULL,
    medicaidID VARCHAR(20) NULL,
    fax VARCHAR(30) NULL,
    raceCode VARCHAR(20) NULL,
    raceDataSource VARCHAR(20) NULL,
    caretakerFirstName VARCHAR(300) NULL,
    caretakerLastName VARCHAR(300) NULL,
    caretakerMiddleInitial VARCHAR(100) NULL,
    ethnicityCode VARCHAR(20) NULL,
    ethnicityDatasource VARCHAR(20) NULL,
    spokenLanguage VARCHAR(20) NULL,
    spokenLanguagesourcecode VARCHAR(20) NULL,
    writtenLanguageCode VARCHAR(20) NULL,
    writtenLanguageSourcecode VARCHAR(20) NULL,
    otherLanguage VARCHAR(20) NULL,
    otherLanguageSourcecode VARCHAR(20) NULL,
    isUSCitizen VARCHAR(20) NULL,
    alternateKey1 VARCHAR(200) NULL,
    alternateKey2 VARCHAR(200) NULL,
    alternateKey3 VARCHAR(200) NULL,
    alternateKey4 VARCHAR(200) NULL,
    alternateKey5 VARCHAR(200) NULL,
    alternateKey6 VARCHAR(200) NULL,
    alternateKey7 VARCHAR(200) NULL,
    alternateKey8 VARCHAR(200) NULL,
    alternateKey9 VARCHAR(200) NULL,
    alternateKey10 VARCHAR(200) NULL,
    maskedMemberID VARCHAR(250) NULL,
    enrolleeEducation VARCHAR(100) NULL,
    enrolleeEmployment VARCHAR(100) NULL,
    effectiveStartDate DATE NOT NULL DEFAULT CURRENT_DATE,
    effectiveEndDate DATE NULL,
    isCurrent BOOLEAN NOT NULL DEFAULT TRUE,
    ProductID VARCHAR(100) NULL,
    createdDateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedDateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fullRowHash VARCHAR(64) NULL,
    
    -- Unique constraint for SCD2
    CONSTRAINT uq_member_natural_key UNIQUE (planMemberID, isCurrent, effectiveStartDate)
);

-- Indexes for performance
CREATE INDEX idx_dimmember_planmemberid ON platinum_dimmember(planMemberID);
CREATE INDEX idx_dimmember_beneficiaryid ON platinum_dimmember(beneficiaryID);
CREATE INDEX idx_dimmember_iscurrent ON platinum_dimmember(isCurrent);
CREATE INDEX idx_dimmember_dateofbirth ON platinum_dimmember(dateofBirth);

-- Comments for documentation
COMMENT ON TABLE platinum_dimmember IS 'Member dimension table (SCD Type 2) - stores historical member attributes';
COMMENT ON COLUMN platinum_dimmember.memberKey IS 'Surrogate key (auto-generated)';
COMMENT ON COLUMN platinum_dimmember.planMemberID IS 'Natural key from source system (HICN/Beneficiary ID)';
COMMENT ON COLUMN platinum_dimmember.isCurrent IS 'SCD Type 2 flag: TRUE = current record, FALSE = historical';
