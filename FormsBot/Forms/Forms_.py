# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
#     ElementClickInterceptedException, TimeoutException

# import time
# driver = webdriver.Firefox()
# driver.get('https://forms.office.com/?redirecturl=https%3a%2f%2fforms.office.com%2fPages%2fDesignPage.aspx%3forigin%3dMarketing')
# print("Navigating to page...")

# # Switch to the frame if needed
# driver.switch_to.frame(0)

# try:
#     # Setează un timeout implicit
#     driver.implicitly_wait(15)

#     # Așteaptă până când butonul de submit este vizibil și poate fi clickat
#     submit_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
#     )
#     submit_button.click()

#     # Așteaptă până când câmpul de email este prezent și vizibil
#     email_input = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
#     )
#     print("Email input found...")
#     email_input.send_keys('sabinstan19@gmail.com')

#     # Așteaptă până când butonul de submit este din nou vizibil și poate fi clickat
#     submit_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
#     )
#     submit_button.click()

#     # Așteaptă până când câmpul de parolă este prezent și vizibil
#     password_input = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "i0118"))
#     )
#     password_input.send_keys('123sabinstan')

#     #accepta....
#     accept_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "idSIButton9"))
#     )
#     accept_button.click()

#     #buton de a sta conectat
#     stay_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "acceptButton"))
#     )
#     stay_button.click()
    
#     # Așteaptă până când butonul specificat este prezent și vizibil
#     close_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'css-326'))
#     )
#     close_button.click()

    
#     options = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, 'menu-button-DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAASDPh0VUNUg0NzJGOFdXU1JDSTRQM0REV1QzVjQzNi4u'))
#     )
#     # Apasă pe buton
#     options.click()

#     copy = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ms-ContextualMenu-link") and .//span[text()="Copy"]]'))
#     )
#     # Apasă pe buton
#     copy.click()

#     options2 = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, 'menu-button-DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAASDPh0VUQlU5RDBIVEs2S0k1WFRIUllQMExIUTRFSy4u'))
#     )
#     # Apasă pe buton
#     options2.click()
    
#     open = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Open"]'))
#     )
#     # Apasă pe buton
#     open.click()






#     time.sleep(1000)

# except NoSuchElementException:
#     print("Error: The specified element was not found on the page.")
# except StaleElementReferenceException:
#     print("Error: The element reference is no longer valid; it may have been removed from the DOM.")
# except ElementClickInterceptedException:
#     print("Error: The click on the element was intercepted, possibly by another element.")
# except TimeoutException:
#     print("Error: The operation timed out while waiting for the element.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print('Exiting...')
#     driver.quit()








import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Forms(webdriver.Firefox):
    def __init__(self,teardown=False):
        self.teardown = teardown
        super(Forms, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.ininitial_button_ids=set()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self,base_url):
        self.get(base_url)
        wait = WebDriverWait(self, 20)
        print("Navigating to page...")
        # Switch to the frame if needed
        self.switch_to.frame(0)

    def Sign_in(self,email,password):
        self.implicitly_wait(15)
        # Așteaptă până când butonul de submit este vizibil și poate fi clickat
        submit_button = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
        )
        submit_button.click()

        # Așteaptă până când câmpul de email este prezent și vizibil
        email_input = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
        )
        print("Email input found...")
        email_input.send_keys(email)

        # Așteaptă până când butonul de submit este din nou vizibil și poate fi clickat
        submit_button = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
        )
        submit_button.click()

        # Așteaptă până când câmpul de parolă este prezent și vizibil
        password_input = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.ID, "i0118"))
        )
        password_input.send_keys(password)

        #accepta....
        accept_button = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.ID, "idSIButton9"))
        )
        accept_button.click()

        #buton de a sta conectat
        stay_button = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.ID, "acceptButton"))
        )
        stay_button.click()
      
    def DuplicateTemplate(self):
        # Așteaptă până când butonul specificat este prezent și vizibil
        close_button = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-326'))
        )
        close_button.click()




       
        buttons = self.find_elements(By.CSS_SELECTOR, 'button[id^="menu-button-"]')
        for button in buttons:
            self.ininitial_button_ids.add(button.get_attribute('id'))

        print("ID-uri inițiale colectate:", self.ininitial_button_ids)
        
        self.monitor_new_buttons()
        #merge, functioneaza insa nu imi face nimic pentru ca nu se copiaza nici un alt form!!!!!!!



        

        # options = WebDriverWait(self, 20).until(
        #     EC.element_to_be_clickable((By.ID, 'menu-button-DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAASDPh0VUNUg0NzJGOFdXU1JDSTRQM0REV1QzVjQzNi4u'))
        # )
        # # Apasă pe buton
        # options.click()

        # copy = WebDriverWait(self, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ms-ContextualMenu-link") and .//span[text()="Copy"]]'))
        # )
        # # Apasă pe buton
        # copy.click()
        
        # options2 = WebDriverWait(self, 20).until(
        #     EC.element_to_be_clickable((By.ID, 'menu-button-DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAASDPh0VUQlU5RDBIVEs2S0k1WFRIUllQMExIUTRFSy4u'))
        # )
        # # Apasă pe buton
        # options2.click()
        
        # open = WebDriverWait(self, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Open"]'))
        # )
        # # Apasă pe buton
        # open.click()
        
        time.sleep(100)

    def monitor_new_buttons(self):
        while True:
            current_buttons = self.find_elements(By.CSS_SELECTOR, 'button[id^="menu-button-"]')
            current_button_ids = set(button.get_attribute('id') for button in current_buttons)
            
            # Găsește butoanele noi
            new_button_ids = current_button_ids - self.ininitial_button_ids
            if new_button_ids:
                for new_button_id in new_button_ids:
                    print(f"Buton nou găsit: {new_button_id}")
                    # Apasă pe butonul nou găsit
                    new_button = self.find_element(By.ID, new_button_id)
                    new_button.click()
                    print(f"Apăsat pe butonul nou cu ID: {new_button_id}")
                    # Adaugă noul id la setul de id-uri inițiale pentru a nu apăsa din nou pe același buton
                    self.install_addon.add(new_button_id)
            time.sleep(5)