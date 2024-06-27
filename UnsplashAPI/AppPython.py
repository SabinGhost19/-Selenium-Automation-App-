# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk, ImageOps
# import requests
# import io

# def fetch_images():
#     query = search_entry.get()
#     url = f'http://127.0.0.1:5000/search_photos?query={query}'
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         image_urls = data.get('image_urls', [])
        
#         if not image_urls:
#             messagebox.showinfo("No results", "No images found for the given query.")
#             return

#         # Clear the previous results
#         for widget in canvas_frame.winfo_children():
#             widget.destroy()

#         for img_url in image_urls:
#             try:
#                 image_data = requests.get(img_url).content
#                 image = Image.open(io.BytesIO(image_data))
#                 image = ImageOps.fit(image, (300, 300), Image.LANCZOS)  # Ajustează dimensiunea imaginii
#                 image = ImageOps.expand(image, border=10, fill='white')  # Adaugă margine
#                 img = ImageTk.PhotoImage(image)

#                 img_frame = tk.Frame(canvas_frame, bd=2, relief=tk.RIDGE)
#                 img_frame.pack(side=tk.TOP, padx=10, pady=10)

#                 img_label = tk.Label(img_frame, image=img)
#                 img_label.image = img
#                 img_label.pack()
#             except Exception as e:
#                 print(f"Error loading image from {img_url}: {e}")
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", str(e))

# def on_canvas_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))

# # Set up the GUI
# root = tk.Tk()
# root.title("Unsplash Image Search")
# root.geometry("1024x768")  # Dimensionează fereastra
# root.configure(background='black')

# style = ttk.Style()
# style.configure('TFrame', background='black')
# style.configure('TLabel', background='black', foreground='white', font=('Arial', 14))
# style.configure('TButton', background='blue', foreground='white', font=('Arial', 12), padding=10, relief='flat')
# style.map('TButton', background=[('active', 'darkblue')])
# style.configure('TEntry', fieldbackground='black', foreground='white', font=('Arial', 12), insertcolor='white')

# # Main Frame
# main_frame = ttk.Frame(root, padding="10")
# main_frame.pack(fill=tk.BOTH, expand=True)

# # Search Bar
# search_label = ttk.Label(main_frame, text="Search Query:")
# search_label.grid(row=0, column=0, sticky=tk.W, pady=10)

# search_entry = ttk.Entry(main_frame, width=30)
# search_entry.grid(row=0, column=1, sticky=tk.W, pady=10, padx=5)

# search_button = ttk.Button(main_frame, text="Search", command=fetch_images)
# search_button.grid(row=0, column=2, sticky=tk.W, pady=10, padx=5)

# # Scrollable Canvas for Results
# canvas = tk.Canvas(main_frame, background='black')
# canvas.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

# scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
# scrollbar.grid(row=1, column=3, sticky=(tk.N, tk.S))

# canvas.configure(yscrollcommand=scrollbar.set)

# canvas_frame = ttk.Frame(canvas, style='TFrame')
# canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# canvas_frame.bind("<Configure>", on_canvas_configure)

# root.mainloop()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Inițializează driver-ul pentru browser
driver = webdriver.Firefox()

# Maximizează fereastra browser-ului
driver.maximize_window()

# Accesează pagina principală Wikipedia
driver.get("https://ro.wikipedia.org/wiki/Pagina_principal%C4%83")

# Așteaptă câteva secunde pentru a ne asigura că pagina este complet încărcată
time.sleep(1)
driver.implicitly_wait(20)
# Găsește bara de căutare și introduce locația sau numele
search_box = driver.find_element(By.CSS_SELECTOR, "input.cdx-text-input__input")
search_term = "Madrid"  # Introdu locația sau numele dorit
search_box.send_keys(search_term)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

driver.implicitly_wait(20)
# Obține conținutul paginii
page_content = driver.page_source
# Închide driver-ul
driver.quit()

# Parsează conținutul paginii cu BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Găsește secțiunea "Istorie"
history_section = soup.find('span', {'id': 'Istorie'})
if history_section:
    # Găsește toate paragrafele din secțiunea "Istorie"
    history_paragraphs = []
    next_node = history_section.find_next()
    while next_node:
        if next_node.name == 'h2':
            break  # Ieși din buclă la următorul titlu de nivel 2
        if next_node.name == 'p':
            history_paragraphs.append(next_node.text.strip())
        next_node = next_node.find_next()

    # Afișează toate paragrafele găsite
    for paragraph in history_paragraphs:
        print(paragraph)
else:
    print("Secțiunea 'Istorie' nu a fost găsită pe această pagină.")




# import requests

# def get_city_info(city_name, api_key):
#     url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

#     querystring = {"namePrefix": city_name}

#     headers = {
#         "X-RapidAPI-Key": api_key,
#         "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     data = response.json()
    
#     if data['data']:
#         city_data = data['data'][0]
#         city_id = city_data['id']
#         print(f"City: {city_data['name']}, {city_data['country']}")
#         print(f"Population: {city_data['population']}")
#         print(f"Latitude: {city_data['latitude']}")
#         print(f"Longitude: {city_data['longitude']}")
#     else:
#         print("City not found.")

# if __name__ == "__main__":
#     api_key = "3ada6520d4msh2cb5be7c1337397p1d3458jsn7f27349542a5"
#     city_name = input("Enter the name of the city: ")
#     get_city_info(city_name, api_key)


