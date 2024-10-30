import requests
import json

def fetch_pokemon_data(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    json_data = response.text
    pokemon_data = json.loads(json_data)
    return pokemon_data

# Task 2: Fetching data from the Pokemon API

pikachu = "pikachu"
pikachu_data = fetch_pokemon_data(pikachu)
print(pikachu_data["name"])
print(pikachu_data["abilities"])

# Task 3: Analyzing and Displaying Data

azumarill = "azumarill"
indeedee = "indeedee-male"
marshadow = "marshadow"
pokemon_list = [azumarill, indeedee, marshadow]

def calculate_average_weight(pokemon_list):
    pokemon_num = 0
    pokemon_weight = 0
    for pokemon in pokemon_list:        
        pokemon_data = fetch_pokemon_data(pokemon)
        pokemon_weight += pokemon_data["weight"]
        pokemon_num += 1
    average_weight = pokemon_weight // pokemon_num
    print(f"The average weight of these Pokemon is {average_weight} pounds.")


calculate_average_weight(pokemon_list)

