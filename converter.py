'''
A script that converts currency amounts using fetched exchange rates from fetcher.py.
'''
from logger_config import logger as log
from typing import Dict

'''
A class to convert currency amounts using exchange rates.
'''
def convert( amount: float, exchange_rate: float) -> float:
    if amount < 0:
        log.logger.error("Attempted to convert a negative amount")
        raise ValueError("Amount cannot be negative")
    
    result = amount * exchange_rate
    log.logger.info(f"Converted {amount} at rate {exchange_rate} = {result:.2f}")
    
    return round(result, 2)

