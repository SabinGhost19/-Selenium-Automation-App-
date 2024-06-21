import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, TimeoutException

import time
driver = webdriver.Firefox()
driver.get('https://forms.office.com/?redirecturl=https%3a%2f%2fforms.office.com%2fPages%2fDesignPage.aspx%3forigin%3dMarketing')
print("Navigating to page...")

# Switch to the frame if needed
driver.switch_to.frame(0)

try:
    # Setează un timeout implicit
    driver.implicitly_wait(15)

    # Așteaptă până când butonul de submit este vizibil și poate fi clickat
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
    )
    submit_button.click()

    # Așteaptă până când câmpul de email este prezent și vizibil
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )
    print("Email input found...")
    email_input.send_keys('sabinstan19@gmail.com')

    # Așteaptă până când butonul de submit este din nou vizibil și poate fi clickat
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
    )
    submit_button.click()

    # Așteaptă până când câmpul de parolă este prezent și vizibil
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )
    password_input.send_keys('123sabinstan')

    #accepta....
    accept_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    accept_button.click()

    #buton de a sta conectat
    stay_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "acceptButton"))
    )
    stay_button.click()
    
    # Așteaptă până când butonul specificat este prezent și vizibil
    close_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-326'))
    )
    close_button.click()

    time.sleep(1000)

except NoSuchElementException:
    print("Error: The specified element was not found on the page.")
except StaleElementReferenceException:
    print("Error: The element reference is no longer valid; it may have been removed from the DOM.")
except ElementClickInterceptedException:
    print("Error: The click on the element was intercepted, possibly by another element.")
except TimeoutException:
    print("Error: The operation timed out while waiting for the element.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print('Exiting...')
    driver.quit()
