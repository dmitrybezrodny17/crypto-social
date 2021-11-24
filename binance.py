import requests

def get_price(pair):
    r = requests.get('https://api.binance.com/api/v3/ticker/price')
    pairs = r.json()
    price = [float(i['price']) for i in pairs if i['symbol'] == pair][0]
    return price
