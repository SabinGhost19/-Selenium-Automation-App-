# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import time

# def scrape_lonely_planet(location):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     driver.get(f"https://www.lonelyplanet.com/search?q={location}")
#     time.sleep(3)  # Așteaptă pentru a lăsa pagina să se încarce complet

#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     results = []

#     # Extrage informații din rezultatele căutării
#     for article in soup.find_all('article', class_='card'):
#         title = article.find('h2', class_='card__title').get_text(strip=True)
#         description = article.find('div', class_='card__text').get_text(strip=True)
#         image_url = article.find('img', class_='card__image')['src']
#         link = article.find('a', class_='card__link')['href']
        
#         results.append({
#             'title': title,
#             'description': description,
#             'image_url': image_url,
#             'link': link
#         })

#     driver.quit()
#     return results

# if __name__ == '__main__':
#     location = input("Madrid")
#     results = scrape_lonely_planet(location)
    
#     for result in results:
#         print(f"Title: {result['title']}")
#         print(f"Description: {result['description']}")
#         print(f"Image URL: {result['image_url']}")
#         print(f"Link: {result['link']}")
#         print("="*50)











import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

# Define the location and URL
lonely_planet_url = "https://www.lonelyplanet.com/"

# Initialize the Selenium WebDriver for Firefox
driver = webdriver.Firefox()

# Send the request to the URL using Selenium
driver.get(lonely_planet_url)
# Click pe articolul specificat
try:

    # #onetrust-accept-btn-handler
    # accept=WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    #     )
    # accept.click()

    # time.sleep(5)
    # search_button = WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.ID, 'headlessui-popover-button-:R2jll6:')))
    # search_button.click()

   
   
    # search_input = WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.ID, 'search-lonely-planet-input')))
    # search_input.send_keys('Madrid')
    # search_input.send_keys(Keys.RETURN)

    # first_search_result = WebDriverWait(driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, '(//li[@class="w-full group"])[1]')))
    # first_search_result.click()
       

    # url = 'https://www.lonelyplanet.com/spain/madrid'

    # # Obținerea conținutului paginii
    # response = requests.get(url)
    # response.raise_for_status()  # Verifică dacă cererea a fost realizată cu succes

    # # Parsarea conținutului paginii
    # soup = BeautifulSoup(response.text, 'html.parser')

    # # Extragerea titlului și a paragrafului
    # title = soup.select_one('h1.lg\\:inline').text
    # paragraph = soup.select_one('p.max-w-2xl').text

    # # Afișarea datelor extrase
    # print('Title:', title)
    # print('Paragraph:', paragraph)
    

    # attractions = soup.find_all('div', class_='space-y-4 mt-4')

    # # Extrage informațiile pentru fiecare atracție
    # results = []
    # for attraction in attractions:
    #     title_tag = attraction.find('a', class_='card-link line-clamp-2 w-[80%] md:w-90')
    #     location_tag = attraction.find('p', class_='text-sm font-semibold uppercase !mt-2')
    #     description_tag = attraction.find('p', class_='relative line-clamp-3')
        
    #     title = title_tag.text if title_tag else 'N/A'
    #     location = location_tag.text if location_tag else 'N/A'
    #     description = description_tag.text if description_tag else 'N/A'
        
    #     results.append({
    #         'title': title,
    #         'location': location,
    #         'description': description
    #     })

    # # Afișează rezultatele
    # for result in results:
    #     print(f"Title: {result['title']}")
    #     print(f"Location: {result['location']}")
    #     print(f"Description: {result['description']}")
    #     print('---')



    hotels = "https://www.hotels.com/"
    driver.get(hotels)

    
    accept_btn=WebDriverWait(driver, 20).until(
             EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/button[2]'))
        )
    accept_btn.click()
    
    time.sleep(3)

    # Găsește și face click pe câmpul de căutare
    search_field_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.uitk-form-field-trigger')))
    search_field_button.click()

    # Găsește câmpul de căutare și introduce textul "Madrid"
    search_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.uitk-field-input')))
    search_field.send_keys('Madrid')
    time.sleep(1)
    search_field.send_keys(Keys.DOWN)
    search_field.send_keys(Keys.RETURN)
    time.sleep(1)




    # Așteaptă până când butonul pentru calendar este disponibil și apasă pe el
    calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="uitk-date-selector-input1-default"]'))
    )
    calendar_button.click()
    time.sleep(1)
    # Așteaptă până când calendarul este vizibil
    calendar_visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.uitk-calendar'))
    )

    # Găsește butonul "Next" și apasă pe el până când luna august devine vizibilă
    next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-stid="uitk-calendar-navigation-controls-next-button"]')

    # Navighează la luna august (presupunem că trebuie să apăsăm de 1-2 ori pe butonul "Next")
    for _ in range(1):
        next_button.click()
        time.sleep(1)  # Așteaptă un timp pentru ca tranziția să aibă loc


    #----------------------------------------------------------------------
    # Selectează data de 12 august
    # date_12_aug = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Monday 12 August 2024"]')))
    # date_12_aug.click()

    # # Selectează data de 16 august
    # date_16_aug = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Friday 16 August 2024"]')))
    # date_16_aug.click()

    # # Așteaptă puțin pentru a vizualiza selecția
    # time.sleep(2)
    #----------------------------------------------------------------------------

    # Găsește și face click pe butonul de căutare
    search_button = driver.find_element(By.ID, 'search_button')
    search_button.click()

    # Așteaptă câteva secunde pentru a permite paginii să se încarce rezultatele căutării

    card_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-stid="lodging-card-responsive"]'))
    )

    # Extrage denumirea
    denumire = card_element.find_element(By.CSS_SELECTOR, 'h3.uitk-heading').text

    # Extrage ratingul
    rating_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-rating span.is-visually-hidden')
    rating = rating_element.text.split(" out of ")[0] if rating_element else "N/A"

    # Extrage prețul
    price_element = card_element.find_element(By.CSS_SELECTOR, 'div[data-test-id="price-summary"] div.uitk-text-emphasis-theme')
    pret = price_element.text if price_element else "N/A"

    # Extrage ce au apreciat oaspeții
    liked_element = card_element.find_element(By.CSS_SELECTOR, 'div[data-test-id="price-summary"] div.uitk-layout-flex-align-items-center')
    guest_liked = liked_element.text if liked_element else "N/A"

    # Extrage descrierea
    descriere_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-text-default-theme')
    descriere = descriere_element.text if descriere_element else "N/A"

    # Extrage alte detalii (de exemplu, locația)
    locatie_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-text-default-theme[aria-hidden="false"]')
    locatie = locatie_element.text if locatie_element else "N/A"

    # Extrage detalii adiționale (Fully refundable, Collect stamps etc.)
    additional_details = []
    details_elements = card_element.find_elements(By.CSS_SELECTOR, 'div.uitk-text-positive-theme, div.uitk-text-default-theme[aria-hidden="true"]')
    for detail in details_elements:
        additional_details.append(detail.text)

    # Afișează rezultatele
    print(f"Denumire: {denumire}")
    print(f"Rating: {rating}")
    print(f"Preț: {pret}")
    print(f"Guest liked: {guest_liked}")
    print(f"Descriere: {descriere}")
    print(f"Locație: {locatie}")
    print(f"Detalii adiționale: {', '.join(additional_details)}")


    time.sleep(1000)
    
except Exception as e:
    print("Nu am putut găsi sau face click pe articolul specificat:", e)
    driver.quit()
    exit()





# tripadvisor_url = "https://www.tripadvisor.com/Tourism-g187514-Madrid-Vacations.html"

# # Trimite cererea către URL folosind Selenium
# driver.get(tripadvisor_url)
# time.sleep(5)  # Așteaptă încărcarea paginii

# # Parsează pagina principală folosind BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Extrage informații despre "Things to do"
# things_to_do_section = soup.find("div", {"class": "attractions-carousel-shelf-9pSE5"})
# things_to_do_items = things_to_do_section.find_all("div", class_="attractions-carousel-shelf-Card__container--1z4CG")

# things_to_do = []

# for item in things_to_do_items:
#     title_tag = item.find("div", class_="attractions-carousel-shelf-Card__title--1a8Ni")
#     title = title_tag.text.strip() if title_tag else "N/A"
#     link_tag = item.find("a", class_="attractions-carousel-shelf-Card__titleLink--1s9bX")
#     link = link_tag["href"] if link_tag else "N/A"

#     things_to_do.append({"Title": title, "Link": f"https://www.tripadvisor.com{link}"})

# # Afișează informațiile despre "Things to do"
# print("\nThings to do in Madrid:")
# for thing in things_to_do:
#     print(f"Title: {thing['Title']}")
#     print(f"Link: {thing['Link']}")
#     print("\n" + "-"*50 + "\n")

# # Extrage informații despre "Places to stay"
# places_to_stay_section = soup.find("div", {"class": "hotels-carousel-shelf-2iXyT"})
# places_to_stay_items = places_to_stay_section.find_all("div", class_="hotels-carousel-shelf-Card__container--3SWRN")

# places_to_stay = []

# for item in places_to_stay_items:
#     title_tag = item.find("div", class_="hotels-carousel-shelf-Card__title--2-xu0")
#     title = title_tag.text.strip() if title_tag else "N/A"
#     link_tag = item.find("a", class_="hotels-carousel-shelf-Card__titleLink--3lZP1")
#     link = link_tag["href"] if link_tag else "N/A"

#     places_to_stay.append({"Title": title, "Link": f"https://www.tripadvisor.com{link}"})

# # Afișează informațiile despre "Places to stay"
# print("\nPlaces to stay in Madrid:")
# for place in places_to_stay:
#     print(f"Title: {place['Title']}")
#     print(f"Link: {place['Link']}")
#     print("\n" + "-"*50 + "\n")

# driver.quit()
