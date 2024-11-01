# --- Importar a biblioteca --- #
from pypdf import PdfWriter


def juntar_pdf(pdfs: list) -> object:
    """
    Função responsável por juntar os PDFs em um único arquivo.
    :param pdfs: Lista com os PDFs separados.
    :return: Arquivo único em PDF.
    """
    # --- Criar o merger --- #
    merger = PdfWriter()

    # --- Adicionar o merger os arquivos PDF --- #
    for pdf in pdfs:
        merger.append(pdf)

    # --- Escrever o arquivo PDF único --- #
    merger.write('nome_temp.pdf')
    merger.close()

    # --- Ler de bytes para uma forma legível --- #
    with open('nome_temp.pdf', 'rb') as arquivo:
        pdf_certo = arquivo.read()

    return pdf_certo
