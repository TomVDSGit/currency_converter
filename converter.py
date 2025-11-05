import logging

from typing import Dict

logger = logging.getLogger(__name__)

class CurrencyConverter:

    def convert(self, amount: float, exchange_rate: float) -> float:

        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        result = amount * exchange_rate
        logger.info(f"Converted {amount} at rate {exchange_rate} = {result:.2f}")
        
        return round(result, 2)

