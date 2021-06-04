from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

# You need to install the following packages, line of code below
# pip install PyPDF2 
# pip install fpdf

# Create PDF File
def create_file_pdf():
    text = "This will be the text that will be inside the created PDF document"
    document=FPDF()
    document.add_page()
    document.set_font("Arial", size=15)
    document.cell(200, 10, txt=text, ln=1, align="L")
    document.output("Name_File_PDF.pdf") #example: MyPdf.pdf
    document=FPDF(orientation='P', unit='mm', format='A3')

# encrypt the created PDF file
def secure_pdf(inputFile_PDF, outputFile_PDF, password):
    PDFwriter = PdfFileWriter()
    PDFreader = PdfFileReader(inputFile_PDF)

    for page in range(PDFreader.getNumPages()):
        PDFwriter.addPage(PDFreader.getPage(page))
    PDFwriter.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(outputFile_PDF, 'wb') as fh:
        PDFwriter.write(fh)

# Main
if __name__ == '__main__':
    create_file_pdf()
    secure_pdf(inputFile_PDF='Name_File_PDF.pdf',
    outputFile_PDF='File_encrypted_name.pdf',
    password='Your_password')
