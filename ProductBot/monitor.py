from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL

def send_email(product_name, product_price, target_price):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = f'Price Alert: {product_name}'

    body = f'The price of {product_name} has dropped below {target_price} RON.\nCurrent price: {product_price} RON.'
    msg.attach(MIMEText(body, 'plain'))

    print(f"Sending email for {product_name} with price {product_price} RON (target was {target_price} RON)")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_price(product_name, target_price):
    driver = webdriver.Chrome()  
    driver.get(f"https://altex.ro/cauta/?q={product_name}")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.Products-item'))
        )
        products = driver.find_elements(By.CSS_SELECTOR, '.Products-item')[:5]
        
        for product in products:
            print("\n\n\n\n")
            title = product.find_element(By.CSS_SELECTOR, '.Product-name').text.strip()
            price_text = product.find_element(By.CSS_SELECTOR, '.Price-int').text.strip().replace('.', '').replace(',', '.')
            price = float(price_text)
            
            print(f"Found product: {title} with price {price} RON")
            
            if price < target_price:
                print(f"Price of {title} is below target price. Sending email.")
                send_email(title, price, target_price)
    except Exception as e:
        print(f"Error during price monitoring: {e}")
    finally:
        driver.quit()
