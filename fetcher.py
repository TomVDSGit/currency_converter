'''
A fetcher script that fetches exchange rates from an external API.
'''

import os
import sys
import requests
from dotenv import load_dotenv
from logger_config import logger

def fetch_exchange_rate(base: str, target: str) -> float:
    '''
    Fetch exchange rate from base to target currency.
    '''
    load_dotenv()
    api_key = os.getenv("API_KEY") # Accessing API key from .env file
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={base},{target}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        base_rate = data["rates"].get(base)
        target_rate = data["rates"].get(target)
        log.logger.info(f"Fetched exchange rates: {base}={base_rate}, {target}={target_rate}")
        return target_rate / base_rate # Returns final converstion rate
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        log.logger.critical(f"Error fetching exchange rate: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        log.logger.critical(f"Error fetching exchange rate: {e}")
        sys.exit(1)