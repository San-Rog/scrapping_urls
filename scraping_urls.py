import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@st.cache_resource
def get_driver():
    options = Options()
    options.add_argument("--headless") # Roda sem abrir a janela visual
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=options
    )

if st.button("Scrapping"):
    driver = get_driver()
    driver.get("https://www.tjma.jus.br/")
    time.sleep(3)
    texto_da_pagina = driver.find_element(By.TAG_NAME, "body").text
    st.write(texto_da_pagina)
    driver.quit() 
    