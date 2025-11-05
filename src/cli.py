"""
Script to setup the CLI arguments
"""

import argparse


def cli_args():
    """
    Function setting up the CLI arguments
    """

    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Currency conversion.")

    # Add arguments
    parser.add_argument(
        "--base",
        "-b",
        nargs="?",
        default="USD",
        type=str,
        help="Enter the currency you want to start with e.g USD",
    )
    parser.add_argument(
        "--target",
        "-t",
        nargs="?",
        default="EUR",
        type=str,
        help="Enter the currency you want to convert to e.g EUR",
    )
    parser.add_argument(
        "--amount",
        "-a",
        nargs="?",
        default=100,
        type=float,
        help="Enter the amount of base currency you want to convert e.g 100",
    )
    parser.add_argument(
        "--mock",
        "-m",
        action="store_true",
        help="Use offline data instead of accessing the API",
    )

    # Parse arguments to output
    return parser.parse_args()
