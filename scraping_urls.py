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
        try:
            driver = get_driver()
            driver.get("https://www.tjma.jus.br/")
            time.sleep(5)
            driver.refresh()
            textPages = driver.find_element(By.TAG_NAME, "body").text
            st.write(textPages)
        except Exception as error:
            st.write(error)    
    if st.button("Scrapping Links"):
        try:
            driver = get_driver()
            driver.get("https://www.tjma.jus.br/")
            time.sleep(5)
            driver.refresh()
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                url = link.get_attribute("href")
                if url:
                    st.write(url)
        except Exception as error:
            st.write(error)
    if st.button('close'): 
        try:
           driver.quit()
        except:
            pass
 
if __name__ == '__main__':   
    main()
