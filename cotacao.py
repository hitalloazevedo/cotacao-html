import requests

url = ' https://economia.awesomeapi.com.br/last/{}-BRL'


def pegar_cotacao(moeda:str):
    moeda = moeda.upper().strip()

    response = requests.get(url.format(moeda))
    response_json = response.json()

    preco = str(response_json[f'{moeda}BRL']['bid'])
    preco = f'{preco:.4}'.replace('.', ',')

    
    return preco

