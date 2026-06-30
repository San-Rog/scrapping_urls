import time
import streamlit as st
from selenium import webdriver
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

driver = get_driver()

if st.button("Scrape Target Page"):
    with st.spinner("Fetching data..."):
        try:
            driver.get("https://www.tjma.jus.br")
            page_title = driver.title
            st.success(f"Successfully scraped! Page Title: {page_title}")
            
            # Display target element content
            st.write(driver.page_source[:500]) 
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
