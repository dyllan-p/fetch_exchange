import tkinter as tk
import requests
import re

access_key = ""  # Your fixer.io API key.
url = "https://data.fixer.io/api/latest"
rates_dict = {}


def fetch_exchange(currency: str, base: str) -> str:
    """
    Uses the fixer.io API to get latest exchange value for the
    currencies provided as a list in the base argument and prints
    the results against the currency argument.

    Keyword arguments:
    currency -- the currency to check exchange values against.
    base -- a list of currencies to use as a base currency.
    """
    currency = currency.strip().upper()
    base = filter(None, re.split('[, ]', base.upper()))
    for item in base:
        result = requests.get(url + "?access_key=" + access_key +
                              "&base=" + item + "&symbols=" + currency)
        if result.status_code == 200:
            result = result.json()
            rates_dict[item] = result["rates"][currency]

    for k in rates_dict.items():
        label_result = tk.Label(text=k)
        label_result.pack()


window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("Fetch Exchange")

title = tk.Label(
    text="A python program which uses the fixer.io API\n to fetch and compare exchange values\n of multiple currencies against\n a given currency.",
    width=32,
    height=5
)

currency_label = tk.Label(text="Currency (eg. ZAR)")
currency_entry = tk.Entry()

base_label = tk.Label(text="Base Currencies (eg. USD, EUR, BTC)")
base_entry = tk.Entry()

fetch_button = tk.Button(
    text="Fetch",
    command=lambda: fetch_exchange(currency_entry.get(), base_entry.get())
)


title.pack()
currency_label.pack()
currency_entry.pack()
base_label.pack()
base_entry.pack()
fetch_button.pack(pady=10)

window.mainloop()
