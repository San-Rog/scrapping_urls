import streamlit as st
import requests
from bs4 import BeautifulSoup
import zipfile
import io

st.title("Downloader em Massa com Streamlit e BeautifulSoup")

url = st.text_input("Digite a URL da página:")

if st.button("Buscar e Baixar Arquivos"):
    if url:
        try:
            # 1. Faz a requisição da página
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 2. Localiza os links (Adapte o 'href' e a tag conforme o seu site)
            links = soup.find_all('a', href=True)
            
            # Prepara o arquivo Zip em memória
            zip_buffer = io.BytesIO()
            arquivos_baixados = 0
            
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for link in links:
                    href = link['href']
                    
                    # Filtro para identificar apenas links de arquivos (ex: .pdf, .docx, etc.)
                    if href.endswith('.pdf'): 
                        # Ajuste URL caso o href seja relativo
                        file_url = href if href.startswith('http') else f"{url.rstrip('/')}/{href.lstrip('/')}"
                        
                        # Baixa o conteúdo do arquivo
                        file_response = requests.get(file_url)
                        
                        if file_response.status_code == 200:
                            # Pega o nome do arquivo da URL
                            file_name = file_url.split('/')[-1]
                            # Adiciona ao zip em memória
                            zipf.writestr(file_name, file_response.content)
                            arquivos_baixados += 1
            
            if arquivos_baixados > 0:
                zip_buffer.seek(0)
                # 3. Cria o botão de download no Streamlit
                st.download_button(
                    label="📥 Baixar todos os arquivos (.zip)",
                    data=zip_buffer,
                    file_name="arquivos_baixados.zip",
                    mime="application/zip"
                )
                st.success(f"Sucesso! {arquivos_baixados} arquivos compactados.")
            else:
                st.warning("Nenhum arquivo correspondente foi encontrado na página.")
                
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
    else:
        st.info("Por favor, insira uma URL válida.")
