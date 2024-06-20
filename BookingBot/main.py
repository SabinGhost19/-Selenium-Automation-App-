from booking.booking import Booking
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
import time
from booking.constants import BASE_URL, Nr_of_Adults, Nr_of_kids, DESTINATION, CURRENCY

with Booking(teardown=False) as bot:
    try:
        bot.land_first_page(base_url=BASE_URL)
        bot.change_currency(currency=CURRENCY)
        bot.select_place_to_go(place_to_go=DESTINATION)
        bot.select_ocupancy(nr_of_adults=Nr_of_Adults,nr_of_kids=Nr_of_kids)#!
        # bot.select_dates(check_in_date='2024-10-12',
        #                  check_out_date='2024-10-15')
       

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

