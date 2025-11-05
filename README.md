# Task: Build a Currency Converter CLI Tool

In pods, your task is to construct a simple CLI tool to convert currencies using real-time or mock exchange rates that encapsulates best practices that have been discussed. Currently there is a working version of the tool, however it sits in a sorry state- instead of being modularised, all the code is contained within a single file called `currency_converter.py` and the code generally lacks good software engineering practices. Let's transform this into a piece of software that is production-ready, exhibiting all of the following features:

- Modular code structure
- Logging
- Command-line interface with argparse
- Type hinting
- Unit testing with pytest
- Virtual environment compatibility
- Mock data option for testing offline 

Additionally, use version control technology such as git to facilitate collaboration and tracking the evolution of your codebase. Make sure to commit regularly and use branches for each of the features (e.g. 'testing').

## Ideal Example Usage of the Tool
```bash
python main.py --base USD --target EUR --amount 100
python main.py --base GBP --target JPY --amount 200 --mock
```

## Run Tests

All tests should be executed using pytest. Please test every function, sometimes using many tests (including edge cases), and achieve 100% pass rate when running the following command:
```bash
pytest tests/
```

## Project Structure

The below represents a suggested project structure. The files you need are mostly made as skeletons for you to populate with the relevant code.

```
currency_converter/
├── main.py                      <- where you'll run your application from
├── cli.py                       <- This should handle command line arguments
├── fetcher.py                   <- This should get the exchange rate data
├── converter.py                 <- This should be where your converting functionality lives
├── logger_config.py             <- This is where you can define functionality to configure your logs
├── data/                        <- Host data that will be used for testing here
│   └── mock_rates.json
├── tests/                       <- This should host all of your unit tests to be compatible with pytest
│   └── test_converter.py
├── requirements.txt             <- List your packages and their versions so that others can easily use the software
└── README.md                    <- This document
```

Please note this is just a suggested structure, if you wish to organise the code in a different way then that is completely valid so long as it is logically consistent.

## Getting Set Up

You will need to sign up to get a free API key at https://exchangeratesapi.io/ using the option on the top right of the page. Please then assign the ACCESS KEY variable found in `currency_converter.py` to be equal to access key given after the sign up.