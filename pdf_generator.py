from fpdf import FPDF
from s3 import upload

def generate_pdf(body):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)

    pdf.write(8, str(body))
    dir = 'pdfs'
    pdf_file_name = "preciouf.pdf"
    ruta = dir + '/' + pdf_file_name

    # Se sube a S3

    return upload(pdf.output(pdf_file_name, 'S').encode('latin-1'),ruta)