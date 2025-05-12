import xml.etree.ElementTree as ET
NAMESPACES_XML = {
        "xmlns":"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
        "xmlns:cac":"urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        "xmlns:cbc":"urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
    }
NAMESPACES_FIND = {
    'cac':'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    }
ET.register_namespace("","urn:oasis:names:specification:ubl:schema:xsd:Invoice-2")
ET.register_namespace('cac','urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2')
ET.register_namespace('cbc','urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2')

tree = ET.parse("XRechnungBeispiel.xml")
tree.write("newXRechnungBeispiel.xml")