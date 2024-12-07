import requests
import json

API_KEY = 'RGAPI-d3a2d9ac-14bb-45e8-a93f-42ffdb74e304'
REGION = 'br1'


def obter_informacoes_invocador(nickname):
    url = f'https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f'Erro ao buscar informações: {response.status_code}'
    

def exibir_informacoes(invocador):
    if isinstance(invocador, dict):
        print(f"Nome: {invocador['name']}")
        print(f"ID do invocador: {invocador['id']}")
        print(f"Nivel: {invocador['summonerLevel']}")
        print(f"Data de criação: {invocador['revisionDate']}")
    else:
        print(invocador)


nickname = input('Digite o nome de invocador: ')
informacoes = obter_informacoes_invocador(nickname)
exibir_informacoes(informacoes)