import pandas as pd
import requests
from woocommerce import API
import os
from dotenv import load_dotenv
from datetime import datetime

print("""
  __  __ _ _     _______        _    
 |  \/  (_) |   |__   __|      | |   
 | \  / |_| | _____| |___  __ _| | __
 | |\/| | | |/ / _ \ / __|/ _` | |/ /
 | |  | | |   <  __/ \__ \ (_| |   < 
 |_|  |_|_|_|\_\___|_|___/\__,_|_|\_\
                                     
      
Copyright and licensed by miketsak.gr 2023
""")

# Load environment variables
load_dotenv()
print("Environment variables loaded.")

# WooCommerce API details
store_url = os.getenv("WOO_STORE_URL")
consumer_key = os.getenv("WOO_CONSUMER_KEY")
consumer_secret = os.getenv("WOO_CONSUMER_SECRET")
api_endpoint = f"{store_url}/wp-json/wc/v3/orders"

# User input for date range
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Making the request with date range
params = {
    'after': start_date + 'T00:00:00',
    'before': end_date + 'T23:59:59',
    'per_page': 100  # Adjust per_page to the expected number of orders, or implement pagination
}

print(f"Fetching orders from {start_date} to {end_date}...")
response = requests.get(api_endpoint, auth=(consumer_key, consumer_secret), params=params, timeout=60)
orders = response.json()
print(f"Fetched {len(orders)} orders.")

# Process orders data
orders_data = []
for order in orders:
    email = order['billing']['email'] if 'email' in order['billing'] and order['billing']['email'] else '-'
    order_data = {
        'Name': order['billing']['first_name'] + " " + order['billing']['last_name'],
        'Postal Code': order['billing']['postcode'],
        'City': order['billing']['city'],
        'Address': order['billing']['address_1'],
        'Phone Number': order['billing']['phone'],
        'Quantity of Products': sum(item['quantity'] for item in order['line_items']),
        'Price': order['total'],
        'Order Date': order['date_created'],
        'Email': email,
    }
    orders_data.append(order_data)
print("Orders data processed.")

# Convert to DataFrame
df = pd.DataFrame(orders_data)

# Get current date and time
now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

# Save to CSV
filename = f"orders-{formatted_date_time}.csv"
df.to_csv(filename, index=False)
print(f"Orders saved to {filename} successfully.")
input("Press Enter to exit...")
