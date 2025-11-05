"""
Script to run convert currencies based on command line inputs
"""
from cli import cli_args
from logger_config import logger
from fetcher import fetch_exchange_rate
from converter import convert

def main():
    """
    Function to run the other functions for the required converting functionality
    """

    args = cli_args()
    logger.info(f"Arguments received: base={args.base}, target={args.target}, amount={args.amount}, mock={args.mock}")

    try:
        c_rate = fetch_exchange_rate(args.base, args.target, mock=args.mock) #Conversion Rate
        output = convert(args.amount, c_rate) #Output after conversion
        logger.info(f"Conversion result: {args.amount} {args.base} = {output:.4f} {args.target}")
        print(f"Conversion: {args.amount} {args.base} = {output:.4f} {args.target}")
    except Exception as e:
        logger.critical(f"Critical error during conversion: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()