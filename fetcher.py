'''
A fetcher script that fetches exchange rates from an external API.
'''

import os
import sys
import requests
from dotenv import load_dotenv

def fetch_exchange_rate(base: str, target: str) -> float:
    '''
    Fetch exchange rate from base to target currency.
    '''
    # Accessing API key from .env file
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={base},{target}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        base_rate = data["rates"].get(base)
        target_rate = data["rates"].get(target)
        return target_rate / base_rate
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        sys.exit(1)