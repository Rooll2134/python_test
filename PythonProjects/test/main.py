import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4999b2dad1d176fb3f674d4962ee3b9d'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Чимчар",
    "photo_id": 390
}

body_rename = {
    "pokemon_id": "333038",
    "name": "Чимичунга",
    "photo_id": 399
}
body_pokemons = {
    "pokemon_id": "333038"
}

'''requests_create = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_create)
print(requests_create.text)  '''   

'''requests_rename = requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_rename)
print(requests_rename.text)'''

requests_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokemons)
print(requests_pokeball.text)