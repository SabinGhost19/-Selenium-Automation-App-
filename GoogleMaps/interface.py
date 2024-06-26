import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd
from threading import Thread

class ScrapingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date Extrase")

        self.search_label = ttk.Label(root, text="Căutare:")
        self.search_label.pack(pady=5)
        
        self.search_entry = ttk.Entry(root, width=50)
        self.search_entry.pack(pady=5)

        self.start_button = ttk.Button(root, text="Start Scraping", command=self.start_scraping)
        self.start_button.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("Title", "Address", "Work Hours", "Phone Number", "Review", "Site", "Scor"), show='headings')
        self.tree.heading("Title", text="Title")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Work Hours", text="Work Hours")
        self.tree.heading("Phone Number", text="Phone Number")
        self.tree.heading("Review", text="Review")
        self.tree.heading("Site", text="Site")
        self.tree.heading("Scor", text="Scor")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def start_scraping(self):
        self.start_button.config(state=tk.DISABLED)
        query = self.search_entry.get()
        thread = Thread(target=self.scrape_data, args=(query,))
        thread.start()

    def scrape_data(self, query):
        response = requests.get(f'http://127.0.0.1:5000/scrape?query={query}')
        if response.status_code == 200:
            data = response.json()
            self.update_table(data)
        else:
            print("Eroare la preluarea datelor")
        self.start_button.config(state=tk.NORMAL)

    def update_table(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in data:
            self.tree.insert("", "end", values=(item["Title"], item["Address"], item["Work Hours"], item["Phone Number"], item["Review"], item["Site"], item["Scor"]))

if __name__ == '__main__':
    root = tk.Tk()
    app = ScrapingApp(root)
    root.mainloop()
