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
        submit_button = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
        )
        submit_button.click()

        email_input = WebDriverWait(self, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
        )
        print("Email input found...")
        email_input.send_keys(email)

        submit_button = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and contains(@class, "btn-override")]'))
        )
        submit_button.click()

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

        wait = WebDriverWait(self, 20)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.css-100')))
            print("Main container loaded")
        except:
            print("Main container did not load")
            self.quit()

        # Define the title to search for, normalizing spaces and newlines
        title_to_select = "C112ABCDE - Feedback (2)"

        # Function to normalize titles by stripping and replacing multiple spaces/newlines with a single space
        def normalize_title(title):
            return ' '.join(title.split())

        # Get all item containers
        item_containers = self.find_elements(By.CSS_SELECTOR, 'div.item-element')
        print(f"Found {len(item_containers)} item containers")

        # Initialize selected_element to None
        selected_element = None

        # Loop through each item container
        for item in item_containers:
            try:
                # Find the title element within the container
                title_element = item.find_element(By.CSS_SELECTOR, 'div[data-automation-id="detailTitle"]')
                # Normalize the title attribute
                normalized_title = normalize_title(title_element.get_attribute('title'))
                # Check if the normalized title matches the desired title
                if normalized_title == title_to_select:
                    selected_element = item
                    print(f"Selected Element ID: {selected_element.get_attribute('id')}")
                    print(f"Title: {title_element.get_attribute('title')}")
                    selected_element.click()
                    print("Element clicked successfully.")
                    break
                else:
                    print(f"Title does not match: {normalized_title}")
            except Exception as e:
                print(f"Error finding title element in container: {e}")

        # If the element is not found, print a message
        if not selected_element:
            print("Element with the specified title was not found.")
            options = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.ID, 'menu-button-DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAASDPh0VUNUg0NzJGOFdXU1JDSTRQM0REV1QzVjQzNi4u'))
            )
         # Apasă pe buton
            options.click()

            copy = WebDriverWait(self, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ms-ContextualMenu-link") and .//span[text()="Copy"]]'))
            )
            # Apasă pe buton
            copy.click()
            self.Modify_Title()
            

        
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
        
        
    def Modify_Title(self):
        
        self.implicitly_wait(10)
        button = self.find_element(By.CLASS_NAME, '-oY-328')
        button.click()

        
        # BUTON PENTRU PREVIEW:
        # button = self.find_element(By.CLASS_NAME, 'css-164') # BUTON PENTRU PREVIEW
        # button.click()
        
        # button = self.find_element(By.CSS_SELECTOR, 'button.-oY-328')
        # button.click()

        # button = self.find_element(By.XPATH, '//button[@aria-label="Templates"]')
        # button.click()

        # self.implicitly_wait(10)
        # template = self.find_element(By.CLASS_NAME,'-ZG-226')
        # template.click()

        self.implicitly_wait(10)
        template = self.find_element(By.CLASS_NAME,'-uR-223')
        template.click()

        # template=WebDriverWait(self, 20).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME,'-oj-220'))
        # )
        # template.click()

        time.sleep(10000)

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