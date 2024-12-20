import requests
import json
import pandas as pd
import sqlite3 as db
import sys
import logging
logger = logging.getLogger(__name__)

API_KEY = "244a38bfdc9a4a5db9fd0ac904c38a2c"

def bail(message):
    logger.error(message)
    sys.exit(1)
    
def fetch_currencies():
    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={API_KEY}"

    try:
        response = requests.get(url)
        if (response.status_code != 200):
            bail(f"Failed to fetch currencies: {response.text}")
    except:
        bail("Failed to fetch currencies")
        
    payload = json.loads(response.text)
    return payload

def convert_currencies(json_currencies):
    try:
        df = pd.DataFrame([{"currency": currency, "rate": rate} for (currency, rate) in json_currencies["rates"].items()])

        df["rate"] = pd.to_numeric(df["rate"])
    except:
        bail("Unexpected data in json")
    return df 

def export_currencies(df):
    try:
        con = db.connect("currencies.db")
        df.to_sql("currencies", con, if_exists="replace")
        con.close()
    except:
        bail("Failed to export currencies")
        
def main():
    logging.basicConfig(filename="currencies.log", level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    payload = fetch_currencies()
    df = convert_currencies(payload)
    export_currencies(df)
    logger.info("Currencies exported")

main()