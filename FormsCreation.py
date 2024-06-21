import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, TimeoutException
import time















#os.environ['PATH'] += r"C:\Users\sabin\Desktop\Selenium_Project\SeleniumDrivers\chromedriver_win32"
driver = webdriver.Firefox()

try:
    driver.get('https://www.goodreads.com/search?utf8=%E2%9C%93&query=beautiful')
    print("Navigating to page...")

    wait = WebDriverWait(driver, 20)
    #button = driver.find_element(By.CSS_SELECTOR, 'button[type="button"].gr-iconButton[data-reactid=".22dtjmq959g.0.0.0"]')
#     dismiss_button = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='gr-iconButton' and @data-reactid='.227bq2kbz2s.0.0.0']"))
# )
#     # Click the dismiss button
#     dismiss_button.click()


    wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(15)  
    book_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//tr[@itemscope][@itemtype="http://schema.org/Book"]')))

    # Initialize a list to store book details
    books = []

    # For each book element
    for book_element in book_elements:
        # Select the book title
        title_element = book_element.find_element(By.CSS_SELECTOR, 'a.bookTitle span[itemprop="name"]')
        title = title_element.text

        # Select the book author
        author_element = book_element.find_element(By.CSS_SELECTOR, 'span[itemprop="author"] span[itemprop="name"]')
        author = author_element.text

        # Append title and author to books list
        books.append((title, author))

        # Display title and author in console
        print(f'Title: {title}, Author: {author}')

    # Navigate to libgen
    driver.get('https://libgen.is/')
    print("Navigating to LibGen page...")

    # For each book in books list, enter title and author in the search bar and perform search
    for title, author in books:
        # Locate the search input
        driver.get('https://libgen.is/')
        search_input = driver.find_element(By.NAME, 'req')

        # Enter title and author into the search bar
        search_query = f"{title} {author}"
        search_input.clear()
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1000)
        print("searchinggg...")
       


    acceept_element = driver.find_element(By.ID, 'L2AGLb')
    acceept_element.click()

    textarea_element = driver.find_element(By.ID, 'APjFqb')
    textarea_element.send_keys('Forms')
    textarea_element.send_keys(Keys.RETURN)
    


   
    wait = WebDriverWait(driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@jsname="UWckNb" and @href="https://forms.office.com/"]')))
    link.click()

    driver.implicitly_wait(15)  

    sign_in_element = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-outline-white-primary[data-bi-cn="signin"][data-bi-ecn="Sign in"][data-bi-ct="button"][data-bi-pa="body"][data-bi-bhvr="100"][data-bi-tags=\'{"BiLinkName":"signin"}\'][aria-label="Sign in to Forms"][target="_blank"]')
    sign_in_element.click()

    driver.implicitly_wait(15)  

    #---------
    # submit_button = driver.find_element(By.CSS_SELECTOR, 'div.row.inline-block.no-margin-top-bottom.button-container > input[type="submit"].btn.btn-block.btn-primary.btn-override')
    # submit_button.click()


    email_input = driver.find_element(By.CSS_SELECTOR, 'div.row.margin-bottom-16 > div.form-group.col-md-12.placeholderContainer > input[type="email"].form-control')
    email_input.send_keys("Sabin")
    time.sleep(1000)
    # email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"][class="form-control"][aria-required="true"][spellcheck="false"][autocomplete="off"]')))
    # email_input.click()
    # # Introduce textul "Sabin" în element
    # email_input.send_keys("Sabin")
    

    time.sleep(1000)


    # email_input = driver.find_element(By.XPATH, '//*[@id="placeholder"]/div[2]/div/input')
    # #submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"].btn.btn-block.btn-primary.btn-override')
    # #submit_button.click()

    # driver.implicitly_wait(15)  
    # email_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[2]/div/input')
    # print("Email input found...")
    
    # # Interact with the element
    # email_input.send_keys('sabinstan19@gmail.com')
    # email_input.send_keys(Keys.RETURN)
    # print("Email entered and submitted...")

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

#
# password_input = driver.find_element(By.ID, 'i0118')
# password_input.send_keys('123')
# password_input.send_keys(Keys.RETURN)
# time.sleep(5)  # Adjust sleep time as needed
#
#     # Locate the form named "hh"
# form_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'hh')]")
# if form_elements:
#     form_element = form_elements[0]
#
#     # Perform right-click action to copy
#     actions = ActionChains(driver)
#     actions.context_click(form_element).perform()
#     time.sleep(1)
#
#     # Copy the form
#     copy_option = driver.find_element(By.XPATH, "//span[text()='Copy']")
#     copy_option.click()
#     time.sleep(1)
#
#     # Right-click again to open
#     actions.context_click(form_element).perform()
#     time.sleep(1)
#
#     # Open the form
#     open_option = driver.find_element(By.XPATH, "//span[text()='Open']")
#     open_option.click()
#     time.sleep(5)
#
# else:
#     print("Form with name 'hh' not found")


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