# --- Importar as bibliotecas --- #
import streamlit as st
from obter_pdfs import obter_pdfs
from juntar_pdf import juntar_pdf

# --- Configurações da página --- #
st.set_page_config(page_title='PDF Merger', layout='centered')

# --- Título da página --- #
st.title('PDF Merger')

# --- Campo para selecionar o nome do arquivo final --- #
nome_arquivo_final = st.text_input(label='Nome do arquivo', placeholder='Digite o nome do arquivo final')

# --- Upload do arquivo .zip --- #
upload = st.file_uploader('Escolha um aquivo ZIP', type='pdf', accept_multiple_files=True)

# --- Criar as colunas --- #
c_1, c_2, c_3, c_4, c_5 = st.columns(5)

# --- Botão para juntar os PDFs --- #
with c_3:
    botao = st.button('Juntar')
    if botao:
        # --- Carregar os PDFs --- #
        pdfs = obter_pdfs(upload)

        # --- Juntar os PDFs --- #
        pdf_junto = juntar_pdf(pdfs)

        # --- Baixar o PDF --- #
        st.download_button(
            label='Download',
            data=pdf_junto,
            file_name=f'{nome_arquivo_final}.pdf',
            mime='application/octet-stream'
        )
