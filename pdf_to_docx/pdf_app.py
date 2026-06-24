from flask import Flask, render_template, request, send_file
import os
import io
from logic.motor_docx import convert_docx_to_txt
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def casita():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    archivo_pdf = request.files['pdf_file']

    if archivo_pdf and archivo_pdf.filename.endswith('.pdf'):
        doc = FPDF.Document(archivo_pdf)
        contenido = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        nombre_base = os.path.splitext(archivo_pdf.filename)[0]
        nombre_docx = f"{nombre_base}.docx"

        convert_docx_to_txt(contenido, nombre_docx)

        return_data = io.BytesIO()
        with open(nombre_docx, 'rb') as f:
            return_data.write(f.read())
        return_data.seek(0)
        
        os.remove(nombre_docx)
        
        return send_file(return_data, download_name=nombre_docx, as_attachment=True)

    return "Archivo no válido. Por favor, suba un archivo .pdf.", 400

if __name__ == '__main__':
    app.run(debug=True)
    