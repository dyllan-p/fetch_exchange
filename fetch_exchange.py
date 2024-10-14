import requests

access_key = ""  # Your fixer.io API key.
url = "https://data.fixer.io/api/latest"
rates_dict = {}


def fetch_exchange(currency: str, base: list) -> str:
    """
    Uses the fixer.io API to get latest exchange value for the
    currencies provided as a list in the base argument and prints
    the results against the currency argument.

    Keyword arguments:
    currency -- the currency to check exchange values against.
    base -- a list of currencies to use as a base currency.
    """
    for item in base:
        result = requests.get(url + "?access_key=" + access_key +
                              "&base=" + item + "&symbols=" + currency)
        if result.status_code == 200:
            result = result.json()
            rates_dict[item] = result["rates"][currency]
    return rates_dict


if __name__ == "__main__":
    fetch_exchange(currency="", base=[])
