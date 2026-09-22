# fetch_exchange

The same small task in four versions: fetch the latest exchange rates from the [fixer.io](https://fixer.io) API for a currency against one or more base currencies.

Written to compare how the same HTTP call, JSON parse and error handling look in C, Python and Ruby. A free fixer.io API key is required for all versions.

## Versions

| File | Language | Notes |
|---|---|---|
| `fetch_exchange.py` | Python | Module with a `fetch_exchange(currency, base)` function; returns a dict of rates |
| `tk_fetch_exchange.py` | Python (Tkinter) | Desktop GUI wrapper around the same function |
| `fetch_exchange.rb` | Ruby | Standard library only (`net/http`, `json`); raises on HTTP or API errors |
| `fetch_exchange.c` | C | libcurl; fetches and prints the raw JSON response |

## Usage

### Python

```python
from fetch_exchange import fetch_exchange

rates = fetch_exchange("ZAR", ["USD", "EUR", "GBP"])
# {'USD': 17.9, 'EUR': 19.6, 'GBP': 22.8}
```

Set `access_key` at the top of the file to your fixer.io key.

### Tkinter desktop app

```bash
python3 tk_fetch_exchange.py
```

Enter a currency and a comma-separated list of base currencies in the window.

### Ruby

```bash
ruby fetch_exchange.rb
```

Set `access_key` in the `params` hash, and change the `fetch_exchange_rate('USD', 'ZAR')` call at the bottom of the file as needed.

### C

```bash
gcc -o fetch_exchange fetch_exchange.c -lcurl
./fetch_exchange
```

Set `API_KEY`, `BASE` and `SYMBOLS` at the top of the file. The C version prints the raw JSON; it does not parse it.

## Notes

- These are deliberately minimal. No retries, no caching, no config files.
- fixer.io's free tier only allows EUR as the base currency; the other bases need a paid plan.
- Keys are hardcoded for simplicity. Don't commit yours.

## License

MIT.
