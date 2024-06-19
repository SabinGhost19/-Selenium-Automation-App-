import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Users\sabin\Desktop\Selenium_Project"
                                  r"\SeleniumDrivers\chromedriver_win32",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get("https://www.booking.com")
    def change_currency(self, currency=None):
        try:
            # Locate and click the currency picker button
            currency_button = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
            self.implicitly_wait(2)
            currency_button.click()
            # Wait for the currency options to load
            self.implicitly_wait(15)
            # Locate and click the desired currency button
            euro_button = self.find_element(By.XPATH,
                                            f'//button[@data-testid="selection-item"]//div[contains(text(), "{currency}")]')
            euro_button.click()

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