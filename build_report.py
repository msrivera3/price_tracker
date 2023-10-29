import re
import uuid
import pandas as pd
from datetime import datetime

def price_text_to_number(price_text):
    # Define regular expressions to match thousands separators and decimal points
    thousands_sep_pattern = r'[,.]'
    decimal_point_pattern = r'[.]'

    # keep only numbers, dots and commas
    pattern = r'[^0-9.,]'
    transformed_text = re.sub(pattern, '', price_text)

    # Replace thousands separators with an empty string
    cleaned_price = re.sub(thousands_sep_pattern, '', transformed_text)

    # Replace the first decimal point with a dot
    cleaned_price = re.sub(decimal_point_pattern, '.', cleaned_price, count=1)

    try:
        # Try to convert the cleaned string to a float
        price_number = float(cleaned_price)
        return price_number
    except ValueError:
        # Handle cases where the conversion to float fails
        print(f"Error: Could not convert '{price_text}' to a numeric value.")
        return None


# Dictionary for the requests report

def build_dict(url, price, rectangle, track_days = 30):
     result = {
        "transaction_id": uuid.uuid4(),
        "Date": datetime.now(),
        "Item_url": url,
        "raw_price": price,
        "days_to_track" : track_days,
        "status" : "ACTIVE",
        "rectangle": rectangle
     }
     return result

# Dictionary for the track report
def build_track_dict(transaction_id, price):
     result = {
        "transaction_id": transaction_id,
        "Date": datetime.now(),
        "price": price
     }
     return result

# Save Report
def save_report(filename, data_dict):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)
    df.to_csv(filename, index=False)
