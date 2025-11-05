"""
Script to run convert currencies based on command line inputs
"""
from cli import cli_args
import logger_config as log
from fetcher import fetch_exchange_rate
from converter import convert

logger = logging.getLogger(__name__)

def main():
    """
    Function to run the other functions for the required converting functionality
    """

    args = cli_args()
    # probs need log statement
    logger.debug(f"CLI arguments parsed: base={args.base}, target={args.target}, amount={args.amount}, mock={args.mock}")

    try:
        c_rate = fetch_exchange_rate(args.base, args.target, mock=args.mock) #Conversion Rate
        output = convert(args.amount, c_rate) #Output after conversion
        # probs need log statement
        logger.info(f"Retrieved exchange rate: 1 {args.base} = {c_rate:.4f} {args.target}")

        print(f"Conversion: {args.amount} {args.base} = {output:.4f} {args.target}")
    except Exception as e:
        # probs need log error statement
        print(f"Error: {e}")
        logger.info("Currency converter application terminated with errors")

if __name__ == "__main__":
    main()