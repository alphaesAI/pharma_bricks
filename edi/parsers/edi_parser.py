from lxml import etree
# from pyx12.params import params
# from pyx12.error_handler import errh_null
from .base_parser import BaseParser


class EDIParser(BaseParser):

    def parse(self, file_path: str):
        xml_root = etree.Element("EDI")

        with open(file_path, "r") as file:
            edi_data = file.read()

        segments = edi_data.split("~")

        for segment in segments:
            segment = segment.strip()

            if not segment:
                continue

            elements = segment.split("*")
            segment_name = elements[0]

            seg_element = etree.SubElement(xml_root, segment_name)

            for index, value in enumerate(elements[1:], start=1):
                child = etree.SubElement(seg_element, f"{segment_name}{index:02}")
                child.text = value

        tree = etree.ElementTree(xml_root)
        tree.write("output.xml", pretty_print=True)

        return xml_root