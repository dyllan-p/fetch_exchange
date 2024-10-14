# fetch_exchange

A python & ruby module which uses the fixer.io API to fetch and compare
exchange values against a given currency.
<https://fixer.io> API key required (sign up for free).

## Usage

```python3
from fetch_exchange import fetch_exchange
```

### Call function with currency and base currencies

```python3
fetch_exchange("ZAR", "USD", "EUR", "BTC")
```

### Tkinter Version (Desktop App)

1. Add your fixer.io API key
2. Open the app with python3
