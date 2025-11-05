
import requests
import sys

def fetch_exchange_rate(base: str, target: str) -> float:
    ACCESS_KEY = '6c6a0af04670dae9753d4bb4e945b792' # Should the Access Key be stored this way?
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}&symbols={base},{target}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        base_rate = data["rates"].get(base)
        target_rate = data["rates"].get(target)
        return target_rate / base_rate
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        sys.exit(1)
    

def main():

    base = input("Enter base currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()

    rate = fetch_exchange_rate(base, target)
    print(f"1 {base} = {rate} {target}")

if __name__ == "__main__":
    main()
