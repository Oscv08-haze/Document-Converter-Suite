from fpdf import FPDF

def generar_pdf(contenido_texto, ruta_salida):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    texto_limpio = contenido_texto.replace('\u2019', "'").replace('\u2018', "'")
    pdf.multi_cell(0, 10, texto_limpio)
    pdf.output(ruta_salida)

    