from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array
from pathlib import Path

pdf = Pdf.open(".pdfs/49.108-20230228-43.004.pdf")

filespec = AttachedFileSpec.from_filepath(pdf, Path("XRechnungBeispiel.xml"))
print(filespec)
pdf.attachments["XRechnungBeispiel.xml"] = filespec
pdf.save("new.pdf")
pdf.close()
