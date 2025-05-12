import pikepdf

pdfDoc = pikepdf.open(".pdfs/G-07-20230228-jsa-49.108.pdf")
with open("XRechnungBeispiel.xml","r") as file:
    pdfDoc.attach(file, file.read())
pdfDoc.save(".pdfs/newZugpferdFile.pdf")