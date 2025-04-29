import json
import requests

class Gestorjson:
    def __init__(self, arch):
        self.arch = arch

    def leerjson(self):
        try:
            with open(self.arch, 'r') as f: 
                return json.load(f)
        except FileNotFoundError:
               print("Archivo no existe")
               return{}
        except json.JSONDecodeError:
               print("El archivo no es Json")
               return{}
    
    def escribir(self, datos):
        with open(self.arch, 'w') as f:
             return json.dump(datos, f, indent=4)
    
    def modificarjson(self,llave,valor):
         datos=self.leerjson()
         datos[llave]=valor
         self.escribir(datos)
        
    def obtenerPokemon(self,pokemon):
        try:
             url= f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
             response=requests.get(url)
             response.raise_for_status()
             data=response.json()
             self.escribir(data)
        except requests.exceptions.HTTPError:
             print("El enlce no existe")
        except requests.exceptions.RequestException:
             print("No se pudo realizar la petición")

gjson = Gestorjson("pokemon.json")
gjson.obtenerPokemon("Pikachu")
Pokemoninfo= gjson.leerjson()
print(Pokemoninfo)

nombrePokemon = Pokemoninfo.get("name")  
print(f"Nombre del Pokémon: {nombrePokemon}")
