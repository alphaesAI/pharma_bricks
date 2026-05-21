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
        Loads a schema and returns field definitions sorted by OrdinalPosition
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
        Heuristically check if a field name represents a date column
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
        Formats a value based on the field name and schema's DataType
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
        
        with open(output_csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            
            # Since mapped_member has scalar values, let's build the row
            row = []
            for field in fields:
                field_name = field["FieldName"]
                data_type = field.get("DataType", "string")
                
                # Fetch value
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
        Handles multiple claims and groups their respective service lines.
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

        # 2. Group service line indices by claim sequentially using the universal line number reset rule
        service_line_block = mapped_claims.get("service_lines", {})
        line_numbers_list = service_line_block.get("line_number", [])
        if not isinstance(line_numbers_list, list):
            line_numbers_list = [line_numbers_list] if line_numbers_list else []

        claims_service_lines = []
        current_claim_lines = []
        prev_line_num = 0

        for idx, ln in enumerate(line_numbers_list):
            try:
                line_num = int(ln)
            except ValueError:
                line_num = 1
                
            if line_num <= prev_line_num:
                # Sequence reset indicates next claim
                claims_service_lines.append(current_claim_lines)
                current_claim_lines = []
                
            current_claim_lines.append(idx)
            prev_line_num = line_num
            
        if current_claim_lines:
            claims_service_lines.append(current_claim_lines)

        # Pad claims_service_lines to match num_claims if there are empty claims
        while len(claims_service_lines) < num_claims:
            claims_service_lines.append([])

        # 3. Write rows to CSV
        with open(output_csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
            
            for claim_idx in range(num_claims):
                service_line_indices = claims_service_lines[claim_idx]
                
                # If a claim has no service lines, output at least one row with empty line fields
                loop_count = max(1, len(service_line_indices))
                
                for line_loop_idx in range(loop_count):
                    row = []
                    
                    # Determine service line index for this row
                    svc_idx = service_line_indices[line_loop_idx] if service_line_indices else None
                    
                    for field in fields:
                        field_name = field["FieldName"]
                        data_type = field.get("DataType", "string")
                        
                        val = ""
                        
                        # A. Core template
                        if field_name == "TEMPLATE":
                            val = "TEMPLATE"
                            
                        # B. Service Line fields
                        elif field_name == "ClaimLineNumber" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("line_number"), svc_idx)
                        elif field_name == "ProcedureCode" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("procedure_code"), svc_idx)
                        elif field_name == "CPTMod1Line" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("modifier_1"), svc_idx)
                        elif field_name == "CPTMod2Line" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("modifier_2"), svc_idx)
                        elif field_name == "CPTMod3Line" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("modifier_3"), svc_idx)
                        elif field_name == "CPTMod4Line" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("modifier_4"), svc_idx)
                        elif field_name == "BilledAmountLine" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("line_charge_amount"), svc_idx)
                        elif field_name == "LiUomQual" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("unit_measurement_code"), svc_idx)
                        elif field_name == "LiServiceUnitCnt" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("service_unit_count"), svc_idx)
                        elif field_name == "LiDiagcdPtr1" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("diagnosis_code_pointer_1"), svc_idx)
                        elif field_name == "LiDiagcdPtr2" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("diagnosis_code_pointer_2"), svc_idx)
                        elif field_name == "LiDiagcdPtr3" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("diagnosis_code_pointer_3"), svc_idx)
                        elif field_name == "LiDiagcdPtr4" and svc_idx is not None:
                            val = self._get_scalar_or_list_val(service_line_block.get("diagnosis_code_pointer_4"), svc_idx)
                        elif field_name == "ClaimLineRecordType":
                            val = "LINE"
                        elif field_name == "ClaimLineEncounterICN":
                            val = self._get_scalar_or_list_val(encounter_icns, claim_idx)
                            
                        # C. Rendering Provider fields
                        elif field_name == "ClaimLineRenderingProviderLastName":
                            val = mapped_claims.get("RenderingProviderLastName", "")
                        elif field_name == "ClaimLineRenderingProviderFirstName":
                            val = mapped_claims.get("RenderingProviderFirstName", "")
                        elif field_name == "ClaimLineRenderingProviderNPI":
                            val = mapped_claims.get("RenderingProviderNPI", "")
                            
                        # D. Claim Header fields
                        elif field_name in mapped_claims:
                            val = self._get_scalar_or_list_val(mapped_claims[field_name], claim_idx)
                            
                        # Format and append
                        formatted_val = self._format_value(val, field_name, data_type)
                        row.append(formatted_val)
                        
                    writer.writerow(row)
                    
        print(f"Successfully generated Claims CSV: {output_csv_path}")
