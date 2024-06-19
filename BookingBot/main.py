from booking.booking import Booking
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
import time

with Booking(teardown=False) as bot:
    try:
        bot.land_first_page()
        bot.change_currency(currency='GBP')
        bot.select_place_to_go(place_to_go='New York')
        bot.select_dates(check_in_date='2024-10-12',
                         check_out_date='2024-10-15')

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

