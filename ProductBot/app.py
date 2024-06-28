from flask import Flask, render_template, request
from monitor import monitor_price
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monitor', methods=['POST'])
def monitor():
    product_name = request.form['product_name']
    target_price = float(request.form['target_price'])

    print(f"Starting initial monitoring for {product_name} with target price {target_price} RON")
    
    def initial_monitor():
        monitor_price(product_name, target_price)
        print("Initial monitoring completed")

    threading.Thread(target=initial_monitor).start()
    threading.Thread(target=recurring_monitor, args=(product_name, target_price)).start()

    return f"Monitoring started for product: {product_name} with target price: {target_price} RON"

def recurring_monitor(product_name, target_price):
    while True:
        print(f"Recurring monitoring for {product_name} with target price {target_price} RON")
        time.sleep(3600)  # o ora
        monitor_price(product_name, target_price)

if __name__ == "__main__":
    app.run(debug=True)
