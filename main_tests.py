import pdfplumber

with pdfplumber.open("G-07-20230228-jsa-49.108.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
