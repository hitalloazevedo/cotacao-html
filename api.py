import requests

url = 'https://economia.awesomeapi.com.br/json/last/'

def getPrice(coinCode: str):
    coinCode = coinCode.upper()

    try:
        response = requests.get(url + coinCode)
    except:
        print("Request Error")
        exit(1)
        
    data = response.json()

    price = float(data[f'{coinCode}BRL']['bid'])

    return round(price, 2)
