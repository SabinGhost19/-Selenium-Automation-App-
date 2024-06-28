# scraping_selenium.py
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def scrape_wikipedia(location):
    results = []
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://ro.wikipedia.org/wiki/Pagina_principal%C4%83")
    time.sleep(1)
    driver.implicitly_wait(20)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input.cdx-text-input__input")
    search_box.send_keys(location)
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

def scrape_hotels(location):
    properties_details = []

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.hotels.com/")
    time.sleep(1)
    driver.implicitly_wait(20)

    accept_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/button[2]'))
    )
    accept_btn.click()
    time.sleep(3)

    search_field_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.uitk-form-field-trigger'))
    )
    search_field_button.click()

    search_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.uitk-field-input'))
    )
    search_field.send_keys(location)
    time.sleep(1)
    search_field.send_keys(Keys.DOWN)
    search_field.send_keys(Keys.RETURN)
    time.sleep(1)

    calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="uitk-date-selector-input1-default"]'))
    )
    calendar_button.click()
    time.sleep(1)

    calendar_visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.uitk-calendar'))
    )

    next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-stid="uitk-calendar-navigation-controls-next-button"]')

    for _ in range(1):
        next_button.click()
        time.sleep(1)

    search_button = driver.find_element(By.ID, 'search_button')
    search_button.click()
    time.sleep(3)
    driver.implicitly_wait(100)
    results_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-stid="section-results"]'))
    )
    driver.implicitly_wait(100)
    property_cards = results_section.find_elements(By.CSS_SELECTOR, 'div[data-stid="lodging-card-responsive"]')

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

    driver.quit()
    return properties_details

def scrape_lonely_planet(location):
    results = []

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.lonelyplanet.com/")
    time.sleep(1)
    driver.implicitly_wait(20)

    accept = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
    accept.click()

    time.sleep(3)

    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'headlessui-popover-button-:R2jll6:')))
    search_button.click()

    search_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'search-lonely-planet-input')))
    search_input.send_keys(location)
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.implicitly_wait(10)
    first_search_result = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '(//li[@class="w-full group"])[1]')))
    first_search_result.click()
    time.sleep(5)
    driver.implicitly_wait(20)
    page_content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_content, 'html.parser')

    title = soup.select_one('h1.lg\\:inline').text if soup.select_one('h1.lg\\:inline') else 'N/A'
    paragraph = soup.select_one('p.max-w-2xl').text if soup.select_one('p.max-w-2xl') else 'N/A'

    results.append({'title': title, 'paragraph': paragraph})

    attractions = soup.find_all('div', class_='space-y-4 mt-4')

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

    return results

def scrape_data(location):
    results = scrape_lonely_planet(location)
    properties_details = scrape_hotels(location)
    wikipedia_data = scrape_wikipedia(location)

    return {
        'results': results,
        'properties_details': properties_details,
        'wikipedia_data': wikipedia_data
    }