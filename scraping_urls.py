import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=options
    )
    
def main():
    if st.button("Scrapping Texto"):
        driver = get_driver()
        driver.get("https://www.tjma.jus.br/")
        time.sleep(5)        
        textPages = driver.find_element(By.TAG_NAME, "body").text
        st.write(textPages)
 
if __name__ == '__main__':   
    main()
