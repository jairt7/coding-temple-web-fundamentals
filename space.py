import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets

def print_planet_data(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet["name"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

planets = fetch_planet_data()
print_planet_data(planets)

def find_heaviest_planet(planets):
    planet_weight = 0
    for planet in planets:
        if planet["isPlanet"]:
            if planet["mass"]["massValue"] > planet_weight:
                planet_weight = planet["mass"]["massValue"]
                planet_name = planet["name"]
            else:
                continue
    return planet_name, planet_weight

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} x 10^25 kg.")