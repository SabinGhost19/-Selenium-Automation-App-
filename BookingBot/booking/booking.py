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
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.implicitly_wait(15)
        self.get("https://www.booking.com")
        self.implicitly_wait(15)
    def select_place_to_go(self,place_to_go):

        input_element = self.find_element(By.ID, ':re:')
        input_element.clear()
        input_element.send_keys(place_to_go)
        time.sleep(5)
        self.implicitly_wait(15)

        # input_element.send_keys(Keys.ARROW_DOWN)
        # input_element.send_keys(Keys.RETURN)
        # input_element.send_keys(Keys.RETURN)

        first_option = self.find_element(By.CSS_SELECTOR, '#autocomplete-result-0')
        first_option.click()
        self.implicitly_wait(15)


        search_button = self.find_element(By.CSS_SELECTOR,
                                          'button[type="submit"].bf33709ee1.a190bb5f27.c73e91a7c9.bb5314095f.e47e45fccd.a94fe207f7.f0468e7c65')
        search_button.click()
        self.implicitly_wait(15)

    def select_dates(self, check_in_date, check_out_date):
        # check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        # check_in_element.click()
        #
        # check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        # check_out_element.click()
        self.implicitly_wait(15)

        wait = WebDriverWait(self, 20)
        check_in_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-mode='checkin']")))
        check_in_input.click()

        check_in_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"td[data-date='{check_in_date}']")))
        check_in_element.click()

        check_out_element = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"td[data-date='{check_out_date}']")))
        check_out_element.click()


    def change_currency(self, currency=None):

            currency_button = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
            self.implicitly_wait(2)
            currency_button.click()

            self.implicitly_wait(15)
            euro_button = self.find_element(By.XPATH,
                                            f'//button[@data-testid="selection-item"]//div[contains(text(), "{currency}")]')
            euro_button.click()
            self.implicitly_wait(15)


    # def change_curency(self,currency=None):
    #
    #     currency_button = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
    #     self.implicitly_wait(2)
    #     currency_button.click()
    #
    #     self.implicitly_wait(15)
    #
    #     euro_button = self.find_element(By.XPATH,
    #                                         f'//button[@data-testid="selection-item"]//div[contains(text(), "{currency}")]')
    #     # euro_button = self.find_element(By.XPATH, f'//button[.//span[contains(text(), "{currency}")]]')
    #
    #     # euro_button = self.find_element(By.XPATH,
    #     #                              '//button[contains(@class, "bf33709ee1") and contains(@class, "caf6d5613f") and contains(@class, "cf9dc28f24") and contains(@class, "cce605d4d5") and contains(@class, "d7e4a4e122")]')
    #     euro_button.click()