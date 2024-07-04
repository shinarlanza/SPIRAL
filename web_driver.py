from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class inflow():
    def __init__(self):
        self.service = Service(executable_path='./chromedriver.exe')
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        
    def search_wikipedia(self, query):
        self.driver.get(url="https://www.wikipedia.org")

        # Wait for the search input element to be visible
        wait = WebDriverWait(self.driver, 10)  # Set a 10-second timeout
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchInput"]')))

        search_input.click()
        search_input.send_keys(query)

        # Wait for the search button to be clickable
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-form"]/fieldset/button/i')))
        search_button.click()

        text = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mw-content-text"]/div[1]/p[2]'))).text
        if text=='':
            text = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="mw-content-text"]/div[1]/p[3]'))).text
        text = re.sub("[\(\[].*?[\)\]]", "", text)
        print(text)
        

assist = inflow()
assist.search_wikipedia("Banana")