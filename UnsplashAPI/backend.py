# app.py
from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
from scraping_selenium import scrape_data

load_dotenv()

app = Flask(__name__)

UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_photos', methods=['GET'])
def search_photos():
    query = request.args.get('query')
    unsplash_api_url = f"https://api.unsplash.com/search/photos?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(unsplash_api_url)
    if response.status_code == 200:
        data = response.json()
        image_urls = [result['urls']['regular'] for result in data['results']]
        return jsonify({'image_urls': image_urls})
    else:
        return jsonify({'image_urls': []})

@app.route('/scrape', methods=['GET'])
def scrape():
    location = request.args.get('location')
    data = scrape_data(location)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
