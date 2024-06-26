import tkinter as tk
from tkinter import messagebox, ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def search_location():
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Input Error", "Please enter a location")
        return
    
    try:
        response = requests.post('http://127.0.0.1:5000/get_info', json={'location': location})
        if response.status_code == 200:
            display_results(response.json())
        else:
            messagebox.showerror("Error", f"Failed to fetch data: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_results(results):
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    for result in results:
        title_label = tk.Label(result_frame, text=result['title'], font=('Arial', 14, 'bold'))
        title_label.pack()

        description_label = tk.Label(result_frame, text=result['description'], wraplength=500)
        description_label.pack()

        image_data = requests.get(result['image_url']).content
        image = Image.open(BytesIO(image_data))
        image = image.resize((200, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(result_frame, image=photo)
        image_label.image = photo
        image_label.pack()

        link_label = tk.Label(result_frame, text=result['link'], fg='blue', cursor='hand2')
        link_label.pack()
        link_label.bind("<Button-1>", lambda e, url=result['link']: open_link(url))

def open_link(url):
    import webbrowser
    webbrowser.open(url)

# Setting up the main application window
root = tk.Tk()
root.title("Lonely Planet Scraper")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

location_label = tk.Label(main_frame, text="Enter Location:")
location_label.pack(pady=5)

location_entry = tk.Entry(main_frame, width=50)
location_entry.pack(pady=5)

search_button = tk.Button(main_frame, text="Search", command=search_location)
search_button.pack(pady=10)

result_frame = tk.Frame(main_frame)
result_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
