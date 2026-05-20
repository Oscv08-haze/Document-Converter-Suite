from flask import Flask, render_template, request, send_file
import os
import io
from docx_to_pdf.logic.engine_pdf import add_pdf 
from docx import Document

app = Flask(__name__)

@app.route('/')
def casa():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    archivo_docx = request.files['docx_file']

    if archivo_docx and archivo_docx.filename.endswith('.docx'):
        doc = Document(archivo_docx)
        contenido = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        nombre_base = os.path.splitext(archivo_docx.filename)[0]
        nombre_pdf = f"{nombre_base}.pdf"
        
        add_pdf(contenido, nombre_pdf)
        
        return_data = io.BytesIO()
        with open(nombre_pdf, 'rb') as f:
            return_data.write(f.read())
        return_data.seek(0)
        
        os.remove(nombre_pdf)
        
        return send_file(return_data, download_name=nombre_pdf, as_attachment=True)

    return "Archivo no válido. Por favor, suba un archivo .docx.", 400

if __name__ == '__main__':
    app.run(debug=True)