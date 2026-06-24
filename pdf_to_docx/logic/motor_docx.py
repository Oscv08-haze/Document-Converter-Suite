from docx import document

def convert_docx_to_txt(docx_path, txt_path):
    doc = document.Document(docx_path)
    text_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text_content)