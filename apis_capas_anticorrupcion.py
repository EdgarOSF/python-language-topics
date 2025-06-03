import requests


POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/{}/"


def fetch_pokemon(pokemon_id):
    response = requests.get(POKEMON_API_URL.format(pokemon_id))
    if response.status_code == '200':
        return response.json()
    else:
        return None

pikachu = fetch_pokemon(25)
charizard = fetch_pokemon(6)

print(pikachu)
print(charizard)

pikachu_weight = pikachu['weight'] / 10 # Covert to kilograms
charizard_weight = charizard['weight'] / 10 # Covert to kilograms

if pikachu_weight > charizard_weight:
    print(f'Pikachu is heavier than Charizard ({pikachu_weight} vs {charizard_weight})')
else:
    print(f'Charizard is heavier than Pikachu ({charizard_weight} vs {pikachu_weight})')

