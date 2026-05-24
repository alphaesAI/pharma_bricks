import os
import json
import csv


class CSVConverter:

    def __init__(self, schemas_dir: str):
        self.schemas_dir = schemas_dir
        self.member_schema_path = os.path.join(schemas_dir, "member_7.12_schema.json")
        self.claims_schema_path = os.path.join(schemas_dir, "submitted837professionaloutboundclaims_schema.json")

    def _load_schema_columns(self, schema_path: str) -> list:
        """
        Loads a schema and returns field definitions sorted by OrdinalPosition.
        """
        with open(schema_path, "r") as f:
            schema_data = json.load(f)
        
        # Sort fields by OrdinalPosition. OrdinalPosition -1 (like TEMPLATE) is first.
        fields = sorted(
            schema_data.get("columnNames", []),
            key=lambda x: x.get("OrdinalPosition", 0)
        )
        return fields

    def _is_date_field(self, field_name: str) -> bool:
        """
        Heuristically check if a field name represents a date column.
        """
        name_lower = field_name.lower()
        return (
            "date" in name_lower or
            "dob" in name_lower or
            name_lower.endswith("dt") or
            name_lower.endswith("dtline") or
            "servicefrom" in name_lower or
            "servicethru" in name_lower
        )

    def _format_value(self, value, field_name: str, data_type: str) -> str:
        """
        Formats a value based on the field name and schema's DataType.
        """
        if value is None:
            return ""
        
        val_str = str(value).strip()
        
        # Format date fields to MM/dd/yyyy
        if self._is_date_field(field_name):
            if len(val_str) == 8 and val_str.isdigit():
                # YYYYMMDD
                return f"{val_str[4:6]}/{val_str[6:8]}/{val_str[0:4]}"
            elif len(val_str) == 10 and "-" in val_str:
                # YYYY-MM-DD
                parts = val_str.split("-")
                if len(parts) == 3 and len(parts[0]) == 4:
                    return f"{parts[1]}/{parts[2]}/{parts[0]}"
            return val_str
            
        elif data_type == "integer":
            if not val_str:
                return "0"
            try:
                return str(int(float(val_str)))
            except ValueError:
                return "0"
                
        elif data_type == "decimal":
            if not val_str:
                return "0.00"
            try:
                return f"{float(val_str):.2f}"
            except ValueError:
                return "0.00"
                
        return val_str

    def _get_scalar_or_list_val(self, data, index: int):
        """
        Safely gets the value at index if it is a list, otherwise returns the scalar value itself.
        """
        if data is None:
            return ""
        if isinstance(data, list):
            return data[index] if index < len(data) else ""
        return data

    def convert_members(self, mapped_member: dict, output_csv_path: str):
        """
        Generates member_7.12 CSV file matching the schema.
        """
        fields = self._load_schema_columns(self.member_schema_path)
        headers = [f["FieldName"] for f in fields]

        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
        
        with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            
            row = []
            for field in fields:
                field_name = field["FieldName"]
                data_type = field.get("DataType", "string")
                
                val = mapped_member.get(field_name, "")
                if field_name == "TEMPLATE":
                    val = "TEMPLATE"
                
                formatted_val = self._format_value(val, field_name, data_type)
                row.append(formatted_val)
                
            writer.writerow(row)
            
        print(f"Successfully generated Member CSV: {output_csv_path}")

    def convert_claims(self, mapped_claims: dict, output_csv_path: str):
        """
        Generates denormalized claims CSV containing one row per service line.
        Handles nested arrays of service line dictionaries cleanly.
        """
        fields = self._load_schema_columns(self.claims_schema_path)
        headers = [f["FieldName"] for f in fields]

        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
        
        # 1. Determine number of claims in this mapping
        encounter_icns = mapped_claims.get("EncounterICN", "")
        if isinstance(encounter_icns, list):
            num_claims = len(encounter_icns)
        else:
            num_claims = 1 if encounter_icns else 0
            encounter_icns = [encounter_icns] if encounter_icns else []

        # 2. Extract service lines
        # Works with a clean modern array: [{"line_number": "1", ...}, {"line_number": "2", ...}]
        all_service_lines = mapped_claims.get("service_lines", [])

        # 3. Write rows to CSV
        with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            
            for claim_idx in range(num_claims):
                # Backwards compatible safety guard: check if it's a list of dicts or the old parallel list dict
                if isinstance(all_service_lines, dict):
                    loop_count = max(1, len(all_service_lines.get("line_number", [])))
                else:
                    loop_count = max(1, len(all_service_lines))
                
                for line_idx in range(loop_count):
                    row = []
                    
                    # Safely isolate the single service line object
                    svc_line = {}
                    if isinstance(all_service_lines, list) and line_idx < len(all_service_lines):
                        svc_line = all_service_lines[line_idx]
                    
                    for field in fields:
                        field_name = field["FieldName"]
                        data_type = field.get("DataType", "string")
                        
                        val = ""
                        
                        # A. Core template indicator
                        if field_name == "TEMPLATE":
                            val = "TEMPLATE"
                            
                        # B. Service Line mapping (Detects list-of-dicts vs. legacy flat parallel lists)
                        elif field_name == "ClaimLineNumber":
                            val = svc_line.get("line_number") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("line_number"), line_idx)
                        elif field_name == "ProcedureCode":
                            val = svc_line.get("procedure_code") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("procedure_code"), line_idx)
                        elif field_name == "CPTMod1Line":
                            val = svc_line.get("modifier_1") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("modifier_1"), line_idx)
                        elif field_name == "CPTMod2Line":
                            val = svc_line.get("modifier_2") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("modifier_2"), line_idx)
                        elif field_name == "CPTMod3Line":
                            val = svc_line.get("modifier_3") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("modifier_3"), line_idx)
                        elif field_name == "CPTMod4Line":
                            val = svc_line.get("modifier_4") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("modifier_4"), line_idx)
                        elif field_name == "BilledAmountLine":
                            val = svc_line.get("line_charge_amount") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("line_charge_amount"), line_idx)
                        elif field_name == "LiUomQual":
                            val = svc_line.get("unit_measurement_code") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("unit_measurement_code"), line_idx)
                        elif field_name == "LiServiceUnitCnt":
                            val = svc_line.get("service_unit_count") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("service_unit_count"), line_idx)
                        elif field_name == "LiDiagcdPtr1":
                            val = svc_line.get("diagnosis_code_pointer_1") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("diagnosis_code_pointer_1"), line_idx)
                        elif field_name == "LiDiagcdPtr2":
                            val = svc_line.get("diagnosis_code_pointer_2") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("diagnosis_code_pointer_2"), line_idx)
                        elif field_name == "LiDiagcdPtr3":
                            val = svc_line.get("diagnosis_code_pointer_3") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("diagnosis_code_pointer_3"), line_idx)
                        elif field_name == "LiDiagcdPtr4":
                            val = svc_line.get("diagnosis_code_pointer_4") if isinstance(all_service_lines, list) else self._get_scalar_or_list_val(all_service_lines.get("diagnosis_code_pointer_4"), line_idx)
                        elif field_name == "ClaimLineRecordType":
                            val = "LINE"
                        elif field_name == "ClaimLineEncounterICN":
                            val = self._get_scalar_or_list_val(encounter_icns, claim_idx)
                            
                        # C. Rendering Provider mappings
                        elif field_name == "ClaimLineRenderingProviderLastName":
                            val = mapped_claims.get("RenderingProviderLastName", "")
                        elif field_name == "ClaimLineRenderingProviderFirstName":
                            val = mapped_claims.get("RenderingProviderFirstName", "")
                        elif field_name == "ClaimLineRenderingProviderNPI":
                            val = mapped_claims.get("RenderingProviderNPI", "")
                            
                        # D. Core Claim Header fields fallback
                        elif field_name in mapped_claims:
                            val = self._get_scalar_or_list_val(mapped_claims[field_name], claim_idx)
                            
                        # Format output and secure position layout string 
                        formatted_val = self._format_value(val, field_name, data_type)
                        row.append(formatted_val)
                        
                    writer.writerow(row)
                    
        print(f"Successfully generated Claims CSV: {output_csv_path}")