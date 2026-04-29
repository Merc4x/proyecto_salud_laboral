import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    try:
        z = zipfile.ZipFile(docx_path)
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        text = []
        for node in tree.iter():
            if node.tag.endswith('}t') and node.text:
                text.append(node.text)
        return '\n'.join(text)
    except Exception as e:
        return str(e)

path = r'c:\Users\23429\Downloads\Plan de trabajo y portafolio de servicios _ Soluciones Administrativas en Salud Laboral.docx'
print(extract_text_from_docx(path))
