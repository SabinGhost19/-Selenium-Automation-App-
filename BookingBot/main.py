from booking.booking import Booking
import time

with Booking(teardown=False) as bot:
    bot.land_first_page()
    #time.sleep(5)
    bot.implicitly_wait(15)
    bot.change_currency(currency='GBP')
    print('Exiting...')

time.sleep(5)

