import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b4999b2dad1d176fb3f674d4962ee3b9d'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
trainer_id = '32967'
def test_status_code():
    response =requests.get(url=f'{URL}/trainers',params= {'trainer_id':trainer_id})
    assert response.status_code == 200
  
def test_part_of_response():
    response =requests.get(url=f'{URL}/trainers',params= {'trainer_id':trainer_id})
    assert response.json()["data"][0]["trainer_name"] == 'Пумба2134'
    




    