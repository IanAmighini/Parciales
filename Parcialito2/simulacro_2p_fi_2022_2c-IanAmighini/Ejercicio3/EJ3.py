import requests
import pandas as pd

r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
r.json().keys() #acceso a los nombres clave
r.json()['stats'][0]['stat']['name']
r.json()['stats'][0]['base_stat']

#Parecido al de Entrenador y Aves

class Pokedex:
    def __init__(self, pokemon):
        self.nombre = pokemon
        self.info = None
        self.movimientos = []
        self.estadisticas = {}

    def info_pokemon(self):
        self.info = requests.get("https://pokeapi.co/api/v2/pokemon/" + self.nombre)
        for stat in self.info.json()["stats"]:
            self.estadisticas[stat["stat"]["name"]] = stat["base_stat"]
        for move in self.info.json()["moves"]:
            self.movimientos.append(move["move"]["name"])
        
    def show_info(self):
        print("La lista de movimientos es:")
        for move in self.movimientos:
            print(move)
        print("\nSus estadísticas son:")
        print(pd.DataFrame(self.estadisticas.items()))

bulbasaur = Pokedex("bulbasaur")
pikachu = Pokedex("pikachu")

pikachu.info_pokemon()
bulbasaur.info_pokemon()
pikachu.show_info()
bulbasaur.show_info()