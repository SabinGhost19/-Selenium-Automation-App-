# selenium_scraper.py
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests

def scrape_wikipedia():
    results = []
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://ro.wikipedia.org/wiki/Pagina_principal%C4%83")
    time.sleep(1)
    driver.implicitly_wait(20)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input.cdx-text-input__input")
    search_term = "Madrid"
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.implicitly_wait(20)
    
    page_content = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page_content, "html.parser")
    
    history_section = soup.find('span', {'id': 'Istorie'})
    if history_section:
        history_paragraphs = []
        next_node = history_section.find_next()
        while next_node:
            if next_node.name == 'h2':
                break
            if next_node.name == 'p':
                history_paragraphs.append(next_node.text.strip())
            next_node = next_node.find_next()
        
        for paragraph in history_paragraphs:
            results.append(paragraph)
    else:
        results.append("Secțiunea 'Istorie' nu a fost găsită pe această pagină.")
    
    return results

def scrape_data():
    results = []
    properties_details = []

    # Define the location and URL
    lonely_planet_url = "https://www.lonelyplanet.com/"

    # Initialize the Selenium WebDriver for Firefox
    driver = webdriver.Firefox()

    try:
        # Send the request to the URL using Selenium
        driver.get(lonely_planet_url)
        accept = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        accept.click()

        time.sleep(5)
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'headlessui-popover-button-:R2jll6:')))
        search_button.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'search-lonely-planet-input')))
        search_input.send_keys('Madrid')
        search_input.send_keys(Keys.RETURN)

        first_search_result = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '(//li[@class="w-full group"])[1]')))
        first_search_result.click()

        url = 'https://www.lonelyplanet.com/spain/madrid'

        # Obținerea conținutului paginii
        response = requests.get(url)
        response.raise_for_status()

        # Parsarea conținutului paginii
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extragerea titlului și a paragrafului
        title = soup.select_one('h1.lg\\:inline').text
        paragraph = soup.select_one('p.max-w-2xl').text

        results.append({'title': title, 'paragraph': paragraph})

        attractions = soup.find_all('div', class_='space-y-4 mt-4')

        # Extrage informațiile pentru fiecare atracție
        for attraction in attractions:
            title_tag = attraction.find('a', class_='card-link line-clamp-2 w-[80%] md:w-90')
            location_tag = attraction.find('p', class_='text-sm font-semibold uppercase !mt-2')
            description_tag = attraction.find('p', class_='relative line-clamp-3')

            title = title_tag.text if title_tag else 'N/A'
            location = location_tag.text if location_tag else 'N/A'
            description = description_tag.text if description_tag else 'N/A'

            results.append({
                'title': title,
                'location': location,
                'description': description
            })

        hotels = "https://www.hotels.com/"
        driver.get(hotels)

        accept_btn = WebDriverWait(driver, 20).until(
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
            time.sleep(1)

        # Găsește și face click pe butonul de căutare
        search_button = driver.find_element(By.ID, 'search_button')
        search_button.click()

        # Așteaptă câteva secunde pentru a permite paginii să se încarce rezultatele căutării
        results_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-stid="section-results"]'))
        )

        # Găsește toate cardurile de proprietate în secțiunea de rezultate
        property_cards = results_section.find_elements(By.CSS_SELECTOR, 'div[data-stid="lodging-card-responsive"]')

        # Listează detaliile pentru fiecare proprietate
        for card_element in property_cards:
            try:
                denumire = card_element.find_element(By.CSS_SELECTOR, 'h3.uitk-heading').text

                rating_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-rating span.is-visually-hidden')
                rating = rating_element.text.split(" out of ")[0] if rating_element else "N/A"

                price_element = card_element.find_element(By.CSS_SELECTOR, 'div[data-test-id="price-summary"] div.uitk-text-emphasis-theme')
                pret = price_element.text if price_element else "N/A"

                liked_element = card_element.find_element(By.CSS_SELECTOR, 'div[data-test-id="price-summary"] div.uitk-layout-flex-align-items-center')
                guest_liked = liked_element.text if liked_element else "N/A"

                descriere_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-text-default-theme')
                descriere = descriere_element.text if descriere_element else "N/A"

                locatie_element = card_element.find_element(By.CSS_SELECTOR, 'div.uitk-text-default-theme[aria-hidden="false"]')
                locatie = locatie_element.text if locatie_element else "N/A"

                additional_details = []
                details_elements = card_element.find_elements(By.CSS_SELECTOR, 'div.uitk-text-positive-theme, div.uitk-text-default-theme[aria-hidden="true"]')
                for detail in details_elements:
                    additional_details.append(detail.text)

                properties_details.append({
                    'denumire': denumire,
                    'rating': rating,
                    'pret': pret,
                    'guest_liked': guest_liked,
                    'descriere': descriere,
                    'locatie': locatie,
                    'detalii_aditionale': additional_details
                })

            except Exception as e:
                print(f"Error extracting details for a property card: {e}")
                continue

    except Exception as e:
        print("Nu am putut găsi sau face click pe articolul specificat:", e)
        driver.quit()
        return []

    finally:
        driver.quit()

    wikipedia_data = scrape_wikipedia()
    
    return {
        'results': results,
        'properties_details': properties_details,
        'wikipedia_data': wikipedia_data
    }
