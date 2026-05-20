from flask import Flask, render_template, request, send_file
import os
from txt_to_pdf.logic.motor_pdf import generar_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    archivo_txt = request.files['txt_file']

    if archivo_txt and archivo_txt.filename.endswith('.txt'):
        contenido = archivo_txt.read().decode('utf-8')
        nombre_base = os.path.splitext(archivo_txt.filename)[0]
        nombre_pdf = f"{nombre_base}.pdf"
        generar_pdf(contenido, nombre_pdf)
        return send_file(nombre_pdf, as_attachment=True)
    
    return "Archivo no válido. Por favor, suba un archivo .txt.", 400

if __name__ == '__main__':
    app.run(debug=True)