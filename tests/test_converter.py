import sys
import os
import pytest
from src import main


#     (["--base", "USD", "--target", "EUR", "--amount", "100"]),
#     (["--base", "GBP", "--target", "JPY", "--amount", "200"]),


def test_currency_converter(monkeypatch, capfd):
    simulated_args = ["--base", "USD", "--target", "EUR", "--amount", "100"]
    monkeypatch.setattr("sys.argv", ["main.py"] + simulated_args )

    main.main()
    expected = f"Conversion: 100 USD = {130.2720} EUR"
    actual = capfd.readouterr()

    assert  actual == expected