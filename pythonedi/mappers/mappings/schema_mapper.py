# pyrefly: ignore [missing-import]
from pyedi import SchemaMapper
from .mapping import MAPPING_DEFINITION


class ETLSchemaMapper:

    def __init__(self):
        self.mapper = SchemaMapper(MAPPING_DEFINITION)

    def map(self, structured_json: dict, generic_json: dict = None):
        if generic_json:
            structured_json = self.normalize(structured_json, generic_json)
        
        transformed_json = self.mapper.map(structured_json)
        return transformed_json

    def normalize(self, structured_json: dict, generic_json: dict) -> dict:
        try:
            loop = structured_json.get("detail", {}).get("submitter_NM1_loop", {})
            if not loop:
                return structured_json

            # Extract segments list from the parsed X12 representation
            transactions = generic_json.get("transactions", [])
            if not transactions:
                return structured_json
            
            segments = transactions[0].get("segments", [])

            # Extract entities by traversing the X12 segments sequentially
            billing_provider_n3 = None
            billing_provider_n4 = None
            billing_provider_refs = []
            billing_provider_per = None

            subscriber_n3 = None
            subscriber_n4 = None
            subscriber_refs = []
            subscriber_dmg = None

            submitter_per = None

            current_nm1_code = None

            for seg in segments:
                seg_id = seg.get("segment_id")
                elements = seg.get("elements", {})
                hl_context = seg.get("hierarchical_context", {})
                hl_level = hl_context.get("hl_level") if hl_context else None

                if seg_id == "NM1":
                    current_nm1_code = elements.get("NM101")

                if hl_level == "20" or current_nm1_code == "85":
                    if current_nm1_code == "85":
                        if seg_id == "N3":
                            billing_provider_n3 = seg
                        elif seg_id == "N4":
                            billing_provider_n4 = seg
                        elif seg_id == "REF":
                            billing_provider_refs.append(seg)
                        elif seg_id == "PER":
                            billing_provider_per = seg
                elif hl_level == "22" or current_nm1_code == "IL":
                    if current_nm1_code == "IL":
                        if seg_id == "N3":
                            subscriber_n3 = seg
                        elif seg_id == "N4":
                            subscriber_n4 = seg
                        elif seg_id == "REF":
                            subscriber_refs.append(seg)
                        elif seg_id == "DMG":
                            subscriber_dmg = seg
                elif hl_level is None:
                    if current_nm1_code == "41" and seg_id == "PER":
                        submitter_per = seg

            # Reconstruct top-level NM1 list to match indices expected by mapping.py:
            # 0: Submitter (41)
            # 1: Receiver (40)
            # 2: Billing Provider (85)
            # 3: Subscriber (IL)
            # 4: Payer (PR)
            # 5: Rendering Provider (82)
            raw_nm1 = loop.get("transaction_set_header_NM1", [])
            nm1_by_code = {item.get("entity_identifier_code"): item for item in raw_nm1 if item.get("entity_identifier_code")}
            loop["transaction_set_header_NM1"] = [
                nm1_by_code.get("41", {}),
                nm1_by_code.get("40", {}),
                nm1_by_code.get("85", {}),
                nm1_by_code.get("IL", {}),
                nm1_by_code.get("PR", {}),
                nm1_by_code.get("82", {})
            ]

            # Reconstruct parallel lists with stable positions
            loop["transaction_set_header_N3"] = [
                self._format_n3(billing_provider_n3) if billing_provider_n3 else {},
                self._format_n3(subscriber_n3) if subscriber_n3 else {}
            ]

            loop["transaction_set_header_N4"] = [
                self._format_n4(billing_provider_n4) if billing_provider_n4 else {},
                self._format_n4(subscriber_n4) if subscriber_n4 else {}
            ]

            loop["transaction_set_header_PER"] = [
                self._format_per(submitter_per) if submitter_per else {},
                self._format_per(billing_provider_per) if billing_provider_per else {}
            ]

            ref_list = []
            # 85 (Billing Provider) takes indices 0, 1, 2
            for i in range(3):
                if i < len(billing_provider_refs):
                    ref_list.append(self._format_ref(billing_provider_refs[i]))
                else:
                    ref_list.append({})
            # IL (Subscriber) takes index 3
            if subscriber_refs:
                ref_list.append(self._format_ref(subscriber_refs[0]))
            else:
                ref_list.append({})
            loop["transaction_set_header_REF"] = ref_list

            loop["transaction_set_header_DMG"] = [
                self._format_dmg(subscriber_dmg) if subscriber_dmg else {}
            ]

        except Exception as e:
            print(f"Warning: normalizer encountered an exception: {e}")

        return structured_json

    def _format_n3(self, seg) -> dict:
        elements = seg.get("elements", {})
        return {
            "rendering_provider_address_line_1": elements.get("N301"),
            "rendering_provider_address_line_2": elements.get("N302"),
        }

    def _format_n4(self, seg) -> dict:
        elements = seg.get("elements", {})
        return {
            "rendering_provider_city": elements.get("N401"),
            "rendering_provider_state": elements.get("N402"),
            "rendering_provider_zip_code": elements.get("N403"),
            "country_code": elements.get("N404"),
            "location_qualifier": elements.get("N405"),
            "location_identifier": elements.get("N406"),
            "country_subdivision_code": elements.get("N407"),
        }

    def _format_per(self, seg) -> dict:
        elements = seg.get("elements", {})
        return {
            "contact_function_code": elements.get("PER01"),
            "ordering_provider_contact_name": elements.get("PER02"),
            "communication_number_qualifier_03": elements.get("PER03"),
            "communication_number_04": elements.get("PER04"),
            "communication_number_qualifier_05": elements.get("PER05"),
            "communication_number_06": elements.get("PER06"),
            "communication_number_qualifier_07": elements.get("PER07"),
            "communication_number_08": elements.get("PER08"),
        }

    def _format_ref(self, seg) -> dict:
        elements = seg.get("elements", {})
        return {
            "reference_identification_qualifier": elements.get("REF01"),
            "employer_id": elements.get("REF02"),
            "reference_identification": elements.get("REF02"),
        }

    def _format_dmg(self, seg) -> dict:
        elements = seg.get("elements", {})
        return {
            "date_time_period_format_qualifier": elements.get("DMG01"),
            "patient_birth_date": elements.get("DMG02"),
            "patient_gender_code": elements.get("DMG03"),
            "marital_status_code": elements.get("DMG04"),
            "race_or_ethnicity_code": elements.get("DMG05"),
            "citizenship_status_code": elements.get("DMG06"),
            "country_code": elements.get("DMG07"),
        }