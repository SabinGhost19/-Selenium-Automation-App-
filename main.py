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


# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def init_webdriver():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     return driver
#
# def load_config(site):
#     with open('config.json', 'r') as f:
#         config = json.load(f)
#     return config['sites'].get(site)
#
# def extrage_pret(url, site):
#     config = load_config(site)
#     if not config:
#         raise ValueError(f"Configurația pentru {site} nu a fost găsită.")
#
#     driver = init_webdriver()
#     driver.get(url)
#
#     pret = driver.find_element(By.CSS_SELECTOR, config['price_selector']).text
#     driver.quit()
#
#     pret = pret.replace(config['currency'], '').replace(',', '').strip()
#     return float(pret)
#
# def verifica_preturi(produse):
#     notificari = []
#
#     for produs in produse:
#         url, site, pret_minim, email = produs['url'], produs['site'], produs['pret_minim'], produs['email']
#         try:
#             pret_curent = extrage_pret(url, site)
#             if pret_curent < pret_minim:
#                 notificari.append((produs['produs'], pret_curent, email))
#         except Exception as e:
#             print(f"Eroare la extragerea prețului pentru {url}: {e}")
#
#     return notificari
#
# def trimite_email(produs, pret, email_destinatar):
#     mesaj = MIMEText(f'Pretul produsului {produs} a scazut la {pret} Lei.')
#     mesaj['Subject'] = 'Notificare reducere pret'
#     mesaj['From'] = 'notificari@exemplu.com'
#     mesaj['To'] = email_destinatar
#
#     with smtplib.SMTP('smtp.exemplu.com') as server:
#         server.login('user', 'parola')
#         server.sendmail('notificari@exemplu.com', email_destinatar, mesaj.as_string())
#
# def main():
#     produse = [
#         {'produs': 'Laptop XYZ', 'url': 'https://site1.com/laptop-xyz', 'site': 'site1.com', 'pret_minim': 2000, 'email': 'user@exemplu.com'},
#         {'produs': 'Telefon ABC', 'url': 'https://site2.com/telefon-abc', 'site': 'site2.com', 'pret_minim': 1000, 'email': 'user@exemplu.com'}
#     ]
#
#     notificari = verifica_preturi(produse)
#
#     for notificare in notificari:
#         trimite_email(notificare[0], notificare[1], notificare[2])
#
# if __name__ == "__main__":
#     main()



