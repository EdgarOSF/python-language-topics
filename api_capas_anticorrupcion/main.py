from dataclasses import dataclass

import requests

POKEMON_API_URL = 'https://pokeapi.co/api/v2/pokemon/{}/'

@dataclass
class Pokemon:
    id: int
    name: str
    weight_in_grams: int


def fetch_pokemon(pokemon_id):
    request = requests.get(POKEMON_API_URL.format(pokemon_id))

    if request.status_code == 200:
        data = request.json()
        return Pokemon(data['id'], data['name'], data['weight'] * 10)
    else:
        return None

pikachu = fetch_pokemon(25)
charizard = fetch_pokemon(6)

pikachu_weight = pikachu.weight_in_grams
charizard_weight = charizard.weight_in_grams

if pikachu_weight > charizard_weight:
    print(f'Pikachu is heavier than Charizard! ({pikachu_weight} kg vs {charizard_weight} kg)')
else:
    print(f'Charizard is heavier than Pikachu! ({charizard_weight} kg vs {pikachu_weight} kg)')