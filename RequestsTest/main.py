import requests
import pytest 


URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '77e9de4d027aa7d8960ba17af86b85a0'
HEADER= {'trainer_token': TOKEN, 'Content-Type': 'application/json'}
TRAINER_ID = '32964'
body_registration= {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change={
    "pokemon_id": "316798",
    "name": "ХагиВаги",
    "photo_id": 2
}

body_catch={
    "pokemon_id": "316798"
}

# response=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_registration)
# print(response.text)

# response_change=requests.put(url=f'{URL}/pokemons',headers=HEADER, json=body_change)
# print(response_change.text)


response_catch=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER, json=body_catch)
print(response_catch.text)