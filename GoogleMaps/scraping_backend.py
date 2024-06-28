from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    query = request.args.get('query', default='-')
    
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/maps")

    accpt_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,'//button[@aria-label="Acceptă tot"]'))
            )
    accpt_btn.click()

    search_box = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Nv2PK')))

    results = driver.find_elements(By.CLASS_NAME, 'Nv2PK')[:3]

    data = []
    for result in results:
        try:
            title = result.find_element(By.CLASS_NAME, 'qBF1Pd').text
        except:
            title = None
        try:
            element = result.find_element(By.XPATH, '//span[@role="img" and contains(@aria-label, "stele")]')
            aria_label_text = element.get_attribute('aria-label')
            match = re.search(r'(\d+,\d+|\d+\.\d+)', aria_label_text)
            if match:
                review_score = match.group(1)
            else:
                review_score=0
        except:
            review_score=None
        try:
            result.click()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Io6YTe')))

            details = driver.find_elements(By.CLASS_NAME, 'Io6YTe')
            try:
                work_hours_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Închide la")]')))
                work_hours = work_hours_element.text    
            except:
                work_hours = None
            try:
                address=driver.find_element(By.XPATH, '//div[@class="rogA2c "]//div[@class="Io6YTe fontBodyMedium kR99db "]').text
            except:
                address=None
            try:
                site = details[1].text
            except:
                site = None

            try:
                phone_element = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-item-id][@aria-label[contains(.,"Telefon")]]//div[@class="Io6YTe fontBodyMedium kR99db "]')))

                phone_number = phone_element.text
            except:
                phone_number = None
            
            try:
                reviews_element = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span')))
                reviews = reviews_element.text
                number_of_reviews = reviews.strip('()').split(' ')[0]
            except:
                number_of_reviews = None

            driver.back()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Nv2PK')))
            
        except Exception as e:
            print(f"Eroare la preluarea datelor pentru un rezultat: {e}")
            continue

        data.append({
            'Title': title,
            'Address': address,
            'Work Hours': work_hours,
            'Phone Number': phone_number,
            'Review': number_of_reviews,
            'Site': site,
            'Scor' : review_score
        })
    driver.quit()
    df = pd.DataFrame(data)
    df.to_excel('all_datas.xlsx', index=False)
    print("Datele au fost exportate in all_datas.xlsx")

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)