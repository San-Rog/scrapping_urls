import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

st.title("🌐 Streamlit + Selenium Web Scraper")

# Cache the driver setup to prevent re-downloading on every user interaction
@st.cache_resource
def get_driver():
    options = Options()
    options.add_argument("--headless=new")  # Required for server deployment
    options.add_argument("--no-sandbox")   # Required for Linux containers
    options.add_argument("--disable-dev-shm-usage") # Overcomes limited resource problems
    options.add_argument("--disable-gpu")
    
    # Automatically manages and finds the correct Chromium binary path
    return webdriver.Chrome(
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        options=options
    )

def main():
    driver = get_driver()
    if st.button("Scrapping"):
        driver = get_driver()        
        driver.get("https://www.tjma.jus.br/")
        time.sleep(3)
        texto_da_pagina = driver.find_element(By.TAG_NAME, "body").text
        st.write(texto_da_pagina)
    if st.button("close"):
        driver.quit()      
 
if __name__ == '__main__':
     main()
