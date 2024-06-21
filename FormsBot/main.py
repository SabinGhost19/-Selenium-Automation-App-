from Forms.Forms_ import Forms
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
import time
from Forms.constants import BASE_URL,EMAIL,PASSWORD

with Forms(teardown=False) as bot:
    try:
        bot.land_first_page(base_url=BASE_URL)
        bot.Sign_in(email=EMAIL,password=PASSWORD)
        bot.DuplicateTemplate()

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
        time.sleep(5)
