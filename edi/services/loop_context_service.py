class LoopContextService:

    def __init__(self, xml_root):
        self.xml_root = xml_root

    def build_contexts(self):
        contexts = {
            "2000A": [],
            "2000B": [],
            "2300": []
        }

        current_loop = None

        for segment in self.xml_root:

            if segment.tag == "HL":
                hl_code = segment.findtext("HL03")

                if hl_code == "20":
                    current_loop = "2000A"

                elif hl_code == "22":
                    current_loop = "2000B"

            elif segment.tag == "CLM":
                current_loop = "2300"

            if current_loop:
                contexts[current_loop].append(segment)

        return contexts