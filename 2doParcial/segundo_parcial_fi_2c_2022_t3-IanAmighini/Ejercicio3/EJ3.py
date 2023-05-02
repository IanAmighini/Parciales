import requests

r = requests.get('https://rickandmortyapi.com/api/location/')
r.json().keys()
r.json()['results']

class Guia():
    def __init__(self):
        self.info = requests.get('https://rickandmortyapi.com/api/location')
        self.personas = []
    
    def residentes_de(self, lugar):
        for residente in self.info.json()['results']['name' == lugar]['residents']:
            r1 = requests.get(residente)
            self.personas.append(r1.json()['name'])
        print(self.personas)

guia1 = Guia()
guia1.residentes_de('Earth')

#B) ¿Cuál es el dominio al que estamos consultando?

# El dominio al cual le estamos consultando es rickandmortyapi.com

#C) ¿Cuántos lugares tiene almacenada la api?

print(len(r.json()['results']))

# La api tiene 20 lugares distintos

#D) En la arquitectura cliente-servidor ¿Qué características tiene el servidor?

#La arquitectura cliente-servidor es una arquitectura distribuida, es decir que sus componentes están distribuidos en dos tipos de nodos: los clientes que son muchos y el servidor que es uno.
#Los servidores son los que almacenan y proveen la información o recursos a los clientes.
