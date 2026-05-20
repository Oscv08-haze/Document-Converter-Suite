from fpdf import FPDF

def add_pdf(contenido_texto, ruta_salida):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.multi_cell(0, 10, text=contenido_texto)
    pdf.output(ruta_salida)