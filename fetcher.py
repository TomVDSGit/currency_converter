"""
A fetcher script that fetches exchange rates from an external API.
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv
from logger_config import logger
import logger_config as log


def fetch_exchange_rate(base: str, target: str, mock_file: bool = False) -> float:
    """
    Fetch exchange rate from base to target currency.
    """
    
    if mock_file == True:
        try:
            with open(mock_file, 'r') as file:
                response_data = json.load(file)
        except FileNotFoundError:
            logger.critical(f"Mock file '{mock_file}' not found.")
            sys.exit(1)

    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={base},{target}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            response_data = response.json()
        except requests.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            logger.critical(f"Error fetching exchange rate: {e}")
            sys.exit(1)

    try:
        base_rate = response_data["rates"].get(base)
        target_rate = response_data["rates"].get(target)
        logger.info(f"Fetched exchange rates: {base}={base_rate}, {target}={target_rate}")
        return target_rate / base_rate
    
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        logger.critical(f"Error fetching exchange rate: {e}")
        sys.exit(1)

    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        logger.critical(f"Error fetching exchange rate: {e}")
        sys.exit(1)