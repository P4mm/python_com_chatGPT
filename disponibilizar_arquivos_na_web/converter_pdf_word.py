from pdf2docx import Converter

def converter_pdf_para_docx(pdf_filename, docx_filename):
    # Cria um objeto Converter
    cv = Converter(pdf_filename)

    # Converte o PDF para DOCX
    cv.convert(docx_filename, start=0, end=None)

    # Fecha o objeto Converter
    cv.close()

# Exemplo de uso
pdf_filename = 'relatorio_atividades.pdf'
docx_filename = 'relatorio_atividades.docx'

# Converte o PDF para DOCX
converter_pdf_para_docx(pdf_filename, docx_filename)
