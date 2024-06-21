import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

os.environ['PATH'] += r"C:\Users\sabin\Desktop\Selenium_Project\SeleniumDrivers\chromedriver_win32"

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

element = driver.find_element(By.XPATH, '//a[@href="/selenium-tutorials/page-factory-pattern-in-selenium-webdriver"]')
element.click()

element = driver.find_element(By.XPATH, '//a[@href="/" and @title="Home"]')
element.click()

driver.get("https://www.porsche.com/central-eastern-europe/en/_romania_/")

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
model_elements = soup.select('div.m-107-tile__info-wrapper .m-107-info__headline span')

print('model_name')
for element in model_elements:
    model_name = element.get_text(strip=True)
    print(model_name)

driver.quit()
