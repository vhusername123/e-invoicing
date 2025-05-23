import pikepdf
from pikepdf import Name, Dictionary, Array, Stream

xmlName = "XRechnungBeispiel.xml"
pdfDoc = pikepdf.Pdf.open(".pdfs/49.108-20230228-43.004.pdf")
with open(xmlName, "rb") as file:
    xml_data = file.read()


embedded_file = pdfDoc.make_stream(xml_data)
embedded_file[Name("/Type")] = Name("/EmbeddedFile")
embedded_file[Name("/Subtype")] = Name("/application/xml")
filespec = pdfDoc.make_indirect(
    Dictionary(
        {
            Name("/Type"): Name("/Filespec"),
            Name("/F"): pikepdf.String("ZUGFeRD-invoice.xml"),
            Name("/UF"): pikepdf.String("ZUGFeRD-invoice.xml"),
            Name("/EF"): Dictionary(
                {Name("/F"): embedded_file, Name("/UF"): embedded_file}
            ),
            Name("/Desc"): pikepdf.String("ZUGFeRD invoice in XML format"),
            Name("/AFRelationship"): Name("/Data"),
            Name("/MimeType"): pikepdf.String("application/xml"),
        }
    )
)
pdfDoc.Root[Name("/AF")] = pdfDoc.make_indirect(Array([filespec]))
if "/Names" not in pdfDoc.Root:
    pdfDoc.Root[Name("/Names")] = pdfDoc.make_indirect(Dictionary())

pdfDoc.Root["Names"][Name("/EmbeddedFiles")] = pdfDoc.make_indirect(
    Dictionary({Name("/Names"): [pikepdf.String("ZUGFeRD-invoice.xml"), filespec]})
)
xmp_metadata = """<?xpacket begin='' id='W5M0MpCehiHzreSzNTczkc9d'?>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
  <rdf:Description rdf:about=''
    xmlns:zf='urn:ferd:pdfa:CrossIndustryDocument:invoice:1p0#'
    zf:DocumentFileName='ZUGFeRD-invoice.xml'
    zf:DocumentType='INVOICE'
    zf:ConformanceLevel='BASIC'
    zf:Version='1.0'/>
</rdf:RDF>
<?xpacket end='w'?>
"""

pdfDoc.Root.Metadata = pdfDoc.make_stream(xmp_metadata)
pdfDoc.save("/zugferd_invoice.pdf")
pdfDoc.close()
