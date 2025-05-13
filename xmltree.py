import xml.etree.ElementTree as ET
def newElement(tag,text):
    temp = ET.Element(tag)
    temp.text = text
    return temp
def newElementObjectlist(tagtextsobjectlist):
    templist = []
    for tagtextpair in tagtextsobjectlist:
        temp = ET.Element(tagtextpair["tag"])
        temp.text = tagtextpair["text"]
        templist.append(temp)
    return templist
NAMESPACES_XML = {
        "xmlns":"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
        "xmlns:cac":"urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        "xmlns:cbc":"urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
    }
NAMESPACES_FIND = {
    'cac':'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    }
FIXED_DATA = [
    {
        "tag": "cbc:CustomizationID",
        "text": "urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0"
    },
    {
        "tag": "cbc:ProfileID",
        "text": "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0"
    }
    
]
TEST_FILE = "newFullnewXRechnung.xml"

ET.register_namespace("","urn:oasis:names:specification:ubl:schema:xsd:Invoice-2")
ET.register_namespace('cac','urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2')
ET.register_namespace('cbc','urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2')

root = ET.Element("Invoice",NAMESPACES_XML)
root.extend(newElementObjectlist(FIXED_DATA))


tree = ET.ElementTree(root)
tree.write(".generated/newFullnewXRechnung.xml",xml_declaration=True,encoding="UTF-8")