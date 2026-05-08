from lxml import etree


class XMLUtils:

    @staticmethod
    def pretty_print(xml_root):
        print(etree.tostring(xml_root, pretty_print=True).decode())