from PyPDF2 import PdfReader
def pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def txt(txt_file):
    text = txt_file.read()
    return text
