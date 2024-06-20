import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\sabin\Desktop\Selenium_Project"
                                  r"\SeleniumDrivers\chromedriver_win32",teardown=False):
        #self.driver_path = driver_path
        self.teardown = teardown
        #os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self,base_url):
        self.implicitly_wait(15)
        self.get(base_url)
        wait = WebDriverWait(self, 20)
        accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        accept_button.click()
        print("Clicked the Accept button...")
        self.implicitly_wait(15)


    def select_place_to_go(self,place_to_go):

        input_element = self.find_element(By.ID, ':re:')
        input_element.clear()
        input_element.send_keys(place_to_go)
        time.sleep(1)
        self.implicitly_wait(15)
        wait = WebDriverWait(self, 20)

        # input_element.send_keys(Keys.ARROW_DOWN)
        # input_element.send_keys(Keys.RETURN)
        # input_element.send_keys(Keys.RETURN)

        first_option = self.find_element(By.CSS_SELECTOR, '#autocomplete-result-0')
        first_option.click()
        self.implicitly_wait(15)

       


    def select_ocupancy(self,nr_of_adults=2,nr_of_kids=0):

        self.implicitly_wait(15)
        wait = WebDriverWait(self, 20)

        occupancy_config_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='occupancy-config']")))
        occupancy_config_button.click()
        print("Clicked the occupancy config button...")
        
        #press the add btn for adults
        additional_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bf33709ee1.a190bb5f27.dc0e35d124.a746857c37.e8d0e5d0c1.b81c794d25.b61f401344.f22ffed92e")))
                
        for _ in range(nr_of_adults - 2):
            additional_button.click()
            time.sleep(1) 
        print(f"Clicked the additional button for adults {nr_of_adults - 2} times...")


        #press the add btn for kids
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='occupancy-config']")))
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bf33709ee1') and contains(@class, 'a190bb5f27') and contains(@class, 'dc0e35d124') and contains(@class, 'a746857c37') and contains(@class, 'e8d0e5d0c1') and contains(@class, 'b81c794d25') and contains(@class, 'b61f401344') and contains(@class, 'f22ffed92e')]")))
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@tabindex='-1' and @aria-hidden='true']")))
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bf33709ee1.a190bb5f27.dc0e35d124.a746857c37.e8d0e5d0c1.b81c794d25.b61f401344.f22ffed92e")))
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-hidden='true' and @tabindex='-1' and @type='button' and contains(@class, 'bf33709ee1') and contains(@class, 'a190bb5f27') and contains(@class, 'dc0e35d124') and contains(@class, 'a746857c37') and contains(@class, 'e8d0e5d0c1') and contains(@class, 'b81c794d25') and contains(@class, 'b61f401344') and contains(@class, 'f22ffed92e')]")))
        #additional_kids_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@tabindex='-1' and @aria-hidden='true']//svg[@viewBox='0 0 24 24']")))
        #additional_kids_button = self.find_element(By.XPATH, "//button[@tabindex='-1' and @aria-hidden='true' and @type='button' and contains(@class, 'bf33709ee1') and contains(@class, 'a190bb5f27') and contains(@class, 'dc0e35d124') and contains(@class, 'a746857c37') and contains(@class, 'e8d0e5d0c1') and contains(@class, 'b81c794d25') and contains(@class, 'b61f401344') and contains(@class, 'f22ffed92e')]")
        #additional_kids_button = self.find_element(By.CSS_SELECTOR, "button[tabindex='-1'][aria-hidden='true'][type='button']")
        #additional_kids_button = self.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[2]')
        #additional_kids_button = self.find_element(By.CSS_SELECTOR, "#\\:ri\\: > div > div:nth-child(2) > div.c1b0f4f15d > button.bf33709ee1.a190bb5f27.dc0e35d124.a746857c37.e8d0e5d0c1.b81c794d25.b61f401344.f22ffed92e")
        additional_kids_button = self.find_element(By.CSS_SELECTOR, "#\\:ri\\: > div > div:nth-child(2) > div.c1b0f4f15d > button.bf33709ee1.a190bb5f27.dc0e35d124.a746857c37.e8d0e5d0c1.b81c794d25.b61f401344.f22ffed92e")

        for _ in range(nr_of_kids):
            additional_kids_button.click()
            time.sleep(1)  
        print(f"Clicked the additional button for kids {nr_of_kids} times...")


        #search the destination
        search_button = self.find_element(By.CSS_SELECTOR,
                                          'button[type="submit"].bf33709ee1.a190bb5f27.c73e91a7c9.bb5314095f.e47e45fccd.a94fe207f7.f0468e7c65')
        search_button.click()
        self.implicitly_wait(15)

    def select_dates(self, check_in_date, check_out_date):

            wait = WebDriverWait(self, 20)

            # Open the calendar by clicking the check-in date button
            check_in_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='date-display-field-start']"))
            )
            check_in_button.click()
            print("Opened the calendar...")

            # Select check-in date
            check_in_element = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"span[data-date='{check_in_date}']"))
            )
            check_in_element.click()
            print("Check-in date selected...")

            # Select check-out date
            check_out_element = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"span[data-date='{check_out_date}']"))
            )
            check_out_element.click()
            print("Check-out date selected...")


    def change_currency(self, currency=None):

            wait = WebDriverWait(self, 20)

            currency_button = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
            self.implicitly_wait(2)
            currency_button.click()

            self.implicitly_wait(15)
            euro_button = self.find_element(By.XPATH,
                                            f'//button[@data-testid="selection-item"]//div[contains(text(), "{currency}")]')
            euro_button.click()
            self.implicitly_wait(15)


            dismiss_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")))
            dismiss_button.click()
            print("Clicked the Dismiss sign-in info button...")

