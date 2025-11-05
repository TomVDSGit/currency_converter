"""
Script to run convert currencies based on command line inputs
"""
from cli import cli_args
import logger_config as log
from fetcher import fetch_exchange_rate
from converter import convert

def main():
    """
    Function to run the other functions for the required converting functionality
    """

    args = cli_args()
    log.logger.info(f"Starting conversion: {args.amount} {args.base} to {args.target} (mock={args.mock})")

    try:
        c_rate = fetch_exchange_rate(args.base, args.target, args.mock) #Conversion Rate
        output = convert(args.amount, c_rate) #Output after conversion
        log.logger.info(f"Conversion successful: {args.amount} {args.base} = {output:.4f} {args.target}")
        print(f"Conversion: {args.amount} {args.base} = {output:.4f} {args.target}")
    except Exception as e:
        log.logger.error(f"Error occurred: {e}")
        print(f"Error: {e}")
        log.logger.info("Currency converter application terminated with errors")

if __name__ == "__main__":
    main()