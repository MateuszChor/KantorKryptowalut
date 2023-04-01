import yfinance as yf
# import tablib
import requests

symbol = 'AAPL'
start_date = '2022-04-01'
end_date = '2023-04-01'

data = yf.download(symbol, start=start_date, end=end_date)

print(data)


def get_current_price(currency: str):
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    # key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCPLN"
    key = key + currency
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # print(f"{data['symbol']} price is {data['price']}")
    data = data['price']
    return float(data)

print(get_current_price("BTCEUR"))