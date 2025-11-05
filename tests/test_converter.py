from src import main


def test_currency_converter(monkeypatch, capfd):
    simulated_args = ["--base", "USD", "--target", "EUR", "--amount", "100", "--mock"]
    monkeypatch.setattr("sys.argv", ["main.py"] + simulated_args )

    main.main()
    expected = f"Conversion: 100.0 USD = {87.09:.4f} EUR\n"
    actual = capfd.readouterr().out

    assert  actual == expected


def test_currency_converter_robust(monkeypatch, capfd):
    test_cases = [
        ["--base", "USD", "--target", "EUR", "--amount", "100", "--mock"],
        ["--base", "USD", "--target", "JPY", "--amount", "5", "--mock"],
        ["--base", "USD", "--target", "GBP", "--amount", "120", "--mock"],
        ["--base", "EUR", "--target", "JPY", "--amount", "340", "--mock"],
        ["--base", "EUR", "--target", "GBP", "--amount", "20", "--mock"],
        ["--base", "GBP", "--target", "JPY", "--amount", "20", "--mock"]
    ]

    expected = [f"Conversion: 100.0 USD = {87.09:.4f} EUR\n",
                f"Conversion: 5.0 USD = {687.64:.4f} JPY\n",
                f"Conversion: 120.0 USD = {92.11:.4f} GBP\n",
                f"Conversion: 340.0 EUR = {53693.82:.4f} JPY\n",
                f"Conversion: 20.0 EUR = {17.63:.4f} GBP\n",
                f"Conversion: 20.0 GBP = {3583.21:.4f} JPY\n"
                ]

    actual = []
    
    for args in test_cases:
        monkeypatch.setattr("sys.argv", ["main.py"] + args)
        main.main()
        actual.append(capfd.readouterr().out)
    
    print(actual)
    assert expected == actual

        
