import pandas as pd
from datetime import datetime

class GapsInCareCalculator:
    """
    Calculates Gaps in Care metrics (Hb, BP, numerCnt, denomCnt) from EDI data.
    Aligns with bis-* platinum layer (fact_gaps_in_care).
    """

    # Medical Codes for Measures
    CODES_HBA1C_TEST = ['83036', '83037', 'CPT-83036', 'LOINC-4548-4']
    CODES_BP_SYSTOLIC = ['3074F', '3075F']  # CPT II for Systolic
    CODES_BP_DIASTOLIC = ['3078F', '3079F', '3080F']  # CPT II for Diastolic
    
    # Diabetes Diagnosis Codes (Sample ICD-10)
    CODES_DIABETES = ['E11.9', 'E10.9', 'E11', 'E10', 'E13']

    def __init__(self):
        pass

    def calculate_gaps(self, claims_df, services_df, diagnosis_df):
        """
        Main calculation engine.
        
        Args:
            claims_df: DataFrame of claims
            services_df: DataFrame of service lines
            diagnosis_df: DataFrame of diagnosis codes
            
        Returns:
            fact_gaps_df: DataFrame ready for fact_gaps_in_care table
        """
        results = []

        # 1. Identify Diabetes Population (Denominator for A1c)
        diabetes_claims = diagnosis_df[
            diagnosis_df['principal_diagnosis_code'].str.startswith(tuple(self.CODES_DIABETES), na=False) |
            diagnosis_df['additional_diagnosis_code_2'].str.startswith(tuple(self.CODES_DIABETES), na=False)
        ]['claim_number'].unique()

        # 2. Process Gaps for each claim
        for claim_num in claims_df['claim_number']:
            claim_services = services_df[services_df['claim_number'] == claim_num]
            
            # Check for HbA1c Gap
            is_diabetic = claim_num in diabetes_claims
            hba1c_service = claim_services[claim_services['procedure_code'].isin(self.CODES_HBA1C_TEST)]
            
            if is_diabetic:
                gap_entry = {
                    'claim_number': claim_num,
                    'measure_code': 'HEDIS-A1C',
                    'measure_name': 'Diabetes: Hemoglobin A1c Testing',
                    'denom_cnt': 1,
                    'numer_cnt': 1 if not hba1c_service.empty else 0,
                    'last_hb_val': self._extract_hb_value(hba1c_service),
                    'last_hb_date': self._extract_service_date(hba1c_service)
                }
                results.append(gap_entry)

            # Check for Blood Pressure Gap (e.g., for Hypertension)
            bp_sys_service = claim_services[claim_services['procedure_code'].isin(self.CODES_BP_SYSTOLIC)]
            bp_dia_service = claim_services[claim_services['procedure_code'].isin(self.CODES_BP_DIASTOLIC)]

            if not bp_sys_service.empty or not bp_dia_service.empty:
                gap_entry = {
                    'claim_number': claim_num,
                    'measure_code': 'HEDIS-CBP',
                    'measure_name': 'Controlling High Blood Pressure',
                    'denom_cnt': 1, # Simplified attribution
                    'numer_cnt': 1 if (not bp_sys_service.empty and not bp_dia_service.empty) else 0,
                    'last_bp_sys': self._extract_bp_value(bp_sys_service, 'sys'),
                    'last_bp_dia': self._extract_bp_value(bp_dia_service, 'dia'),
                    'last_bp_date': self._extract_service_date(bp_sys_service if not bp_sys_service.empty else bp_dia_service)
                }
                results.append(gap_entry)

        return pd.DataFrame(results)

    def _extract_hb_value(self, service_row):
        """Extracts Hb value from measurement or code."""
        if service_row.empty:
            return None
        # Logic: If supplemental value is present in 'line_note_text' or similar
        # For now, return a placeholder if code is found
        return 7.5 # Placeholder for logic

    def _extract_bp_value(self, service_row, type='sys'):
        """Extracts BP value from CPT II codes."""
        if service_row.empty:
            return None
        code = service_row.iloc[0]['procedure_code']
        # Map CPT II codes to estimated values
        mapping = {
            '3074F': 120, # < 130
            '3075F': 135, # 130-139
            '3078F': 80,  # < 80
            '3079F': 85,  # 80-89
            '3080F': 95   # >= 90
        }
        return mapping.get(code)

    def _extract_service_date(self, service_df):
        """Extracts and formats service date."""
        if service_df.empty:
            return None
        date_str = service_df.iloc[0]['service_date']
        try:
            return datetime.strptime(date_str, '%Y%m%d').date()
        except:
            return None
