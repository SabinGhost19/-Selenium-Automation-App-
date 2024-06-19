import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# Set up the WebDriver path
os.environ['PATH'] += r"C:\Users\sabin\Desktop\Selenium_Project\SeleniumDrivers\chromedriver_win32"
driver = webdriver.Chrome()


    # Navigate to the form URL
driver.get('https://forms.office.com/Pages/DesignPageV2.aspx?origin=Marketing')

    # Wait for the page to load
time.sleep(8)

    # Find and fill the email input
    #email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"].form-control')
email_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email, phone, or Skype"]')
email_input.click()
email_input.send_keys('sabinstan19@gmail.com')
email_input.send_keys(Keys.RETURN)
time.sleep(3)  # Adjust sleep time as needed

    # Find and fill the password input
password_input = driver.find_element(By.ID, 'i0118')
password_input.send_keys('123')
password_input.send_keys(Keys.RETURN)
time.sleep(5)  # Adjust sleep time as needed

    # Locate the form named "hh"
form_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'hh')]")
if form_elements:
    form_element = form_elements[0]

    # Perform right-click action to copy
    actions = ActionChains(driver)
    actions.context_click(form_element).perform()
    time.sleep(1)

    # Copy the form
    copy_option = driver.find_element(By.XPATH, "//span[text()='Copy']")
    copy_option.click()
    time.sleep(1)

    # Right-click again to open
    actions.context_click(form_element).perform()
    time.sleep(1)

    # Open the form
    open_option = driver.find_element(By.XPATH, "//span[text()='Open']")
    open_option.click()
    time.sleep(5)

else:
    print("Form with name 'hh' not found")


# Close the WebDriver
driver.quit()

# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
# import time
#
#
# os.environ['PATH'] += r"C:\Users\sabin\Desktop\Selenium_Project\SeleniumDrivers\chromedriver_win32"
# driver = webdriver.Chrome()
#
# try:
#     # Navigate to the form URL
#     driver.get('https://forms.office.com/Pages/DesignPageV2.aspx?origin=Marketing')
#
#     # Wait for the page to load
#     #driver.implicitly_wait(5)
#     time.sleep(8)
#     # Find and fill the email input
#     email_input = driver.find_element_by_class_name('form-group col-md-12 placeholderContainer')
#     #email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"][placeholder="Email, phone, or Skype"]')
#     email_input.click()
#     email_input.send_keys('sabinstan19@gmail.com')
#     email_input.send_keys(Keys.RETURN)
#     time.sleep(3)  # Adjust sleep time as needed
#
#     # Find and fill the password input
#     password_input = driver.find_element(By.ID, 'i0118')
#     password_input.send_keys('123')
#     password_input.send_keys(Keys.RETURN)
#     time.sleep(5)  # Adjust sleep time as needed
#
#     # Locate the form named "hh"
#     form_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'hh')]")
#     if form_elements:
#         form_element = form_elements[0]
#
#         # Perform right-click action to copy
#         actions = ActionChains(driver)
#         actions.context_click(form_element).perform()
#         time.sleep(1)
#
#         # Copy the form
#         copy_option = driver.find_element(By.XPATH, "//span[text()='Copy']")
#         copy_option.click()
#         time.sleep(1)
#
#         # Right-click again to open
#         actions.context_click(form_element).perform()
#         time.sleep(1)
#
#         # Open the form
#         open_option = driver.find_element(By.XPATH, "//span[text()='Open']")
#         open_option.click()
#         time.sleep(5)
#
#     else:
#         print("Form with name 'hh' not found")
#
# finally:
#     # Close the WebDriver
#     driver.quit()