import re, glob, os

#Consigna 1
#a)

def subsecuencias(string):
    patron = 'X([a-b]*ab[a-b]*)Y'   #'X(.*?ab.*?)Y'
    return re.findall(patron, string)

print(subsecuencias('XbaaaYjXababYqXbabbbbaaYqXffeey'))

#b)
'''def funcionDeExpresiones_Regulares():
    return re.findal("ag(\d.*?)cta")
print(funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta'))'''

def funcionDeExpresiones_Regulares2(string):
    return re.findall("ag(\d.*?)cta",string)
print(funcionDeExpresiones_Regulares2('aabocaggaaactazu4lggaasag24gra1ndecta'))

#El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python
#La función devuelve NameError al ser ejecutada
#La función devuelve SintaxError al ser ejecutada
#Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['gaaa']
#Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['24gra1nde'] 'X'

#Al corregir la funcion(el findall, que la funcion le llegue un parametro) devuelve 24gra1nde

#Era la 4ta, tenia que cambiar el patron

#Consigna 2
#a)  #Agarra todos los mails, tenia que agarrar solo los gmail
def es_correo(mail):
    return re.search("[a-zA-Z0-9_\.\-]+[@][a-z]+[\.][a-z]{2,}",mail)

def mails(nombre):
    textos = glob.glob('*.txt')
    with open(nombre, 'a') as salida:
        for archivo in textos:
            with open(archivo, 'r') as file:
                for linea in file.readlines():
                    for elem in linea.split():
                        if es_correo(elem) is not None:
                            salida.write(elem + '\n')

mails('base_de_datos.txt')

#b)
#i. ¿Qué tipo de exepción arroja la corrida del script?

#Tira un ValueError y dice que x no esta en la lista y por ende no lo puede sacar

#ii. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 3. ¿Qué otras excepciones deberias considerar?

#Se deberia considerar un TypeError por si no se ingresan listas en los 2 primeros parametros o un elemento que se ueda appendear en el tercero.


#Consigna 3

class EntrenadorPokemon():
    def __init__(self, batallas_ganadas = 0, lista_pokemons = []):
      self.batallas_ganadas = batallas_ganadas
      self.pokemons = lista_pokemons
   
    def get_batallas_ganadas(self):
      return self.batallas_ganadas

    def get_pokemons(self):
      return self.pokemons

    def agregar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
    
    def perder_batalla(self):
        self.batallas_ganadas -= 1
        self.pokemons.remove(self.pokemons[-1])

#a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un objeto de esta clase? ¿Qué mensajes entiende?

#El nombre de la clase es EntrenadorPokemon. El estado son las batallas_ganadas y lista_pokemons. Entiende get_batallas_ganadas y get_pokemons

#b)
Ash = EntrenadorPokemon(25,['pikachu'])
Ash.agregar_pokemon('gengar')
print(Ash.get_pokemons())
Ash.perder_batalla()
print(Ash.get_pokemons())



#Consigna 4

class PacMan:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0

    def comerBolita(self,cantidad):
        self.puntos += cantidad*2
    
    def velocidad(self):
        return 2 + self.puntos / 100
    
    def perderVida(self):
        self.vidas -= 1
        self.puntos = 0
        if self.vidas == 0:
            print('Game Over')

    def comerFantasma(self, fantasma):
        if fantasma == 'Rosa':
            self.puntos += 8
        elif fantasma == 'Verde':
            self.puntos += 6
        elif fantasma == 'Naranja':
            self.puntos += 4
        else:
            self.puntos += 2

pacman = PacMan()
pacman.comerBolita(22)
pacman.perderVida()
pacman.comerFantasma("Rojo")
pacman.comerFantasma("Rosa")
print(pacman.puntos)
pacman.comerBolita(20)
print(pacman.velocidad())
pacman.perderVida()
pacman.perderVida()

class PacManMejorado(PacMan):
    def vidaExtra(self):
        if self.puntos >= 200:
            self.puntos -= 200
            self.vidas += 1
        else:
            return print('Faltan', 200 - self.puntos ,'puntos para ganar una vida extra')
    def velocidad(self):
        return 3 + self.puntos / 100


pacmanMejorado = PacManMejorado()
pacmanMejorado.comerBolita(22)
pacmanMejorado.perderVida()
pacmanMejorado.comerFantasma("Rojo")
pacmanMejorado.comerFantasma("Rosa")
print(pacmanMejorado.puntos)
pacmanMejorado.comerBolita(80)
print(pacmanMejorado.velocidad())
print(pacmanMejorado.vidas)
pacmanMejorado.comerBolita(30)
pacmanMejorado.vidaExtra()
print(pacmanMejorado.vidas)
pacmanMejorado.vidaExtra()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()
pacmanMejorado.perderVida()      


#Consigna 5

#A) Marcá con una [X] la/s opcion/es correcta/s y justifica tu elección:

#Onomatopopih debe hacer push en la terminal
#Onomatopopih debe hacer pull en la terminal
#Onomatopopih debe hacer git push en la terminal
#Onomatopopih debe hacer git pull en la terminal 'X'
#Onomatopopih después de agregar su aporte debe escribir en una terminal git add y luego git commit
#Onomatopopih después de agregar su aporte debe escribir en una terminal git add ., luego git commit -m 'mis aportes' y finalmente git push 'X'

#Primero Onomatopopih tiene que hacer git pull para descargarse la ultima version del repo compartido. Luego el tiene que hacer git add . y git commit -m'' con git push para subir sus aportes al repo asi todos se lo pueden bajar


#Al tiempo, Onomatopopih descubrió que sus compañeros actualizaron elrepositorio. Marcá con una [X] la/s opcion/es correcta/s y justifica tu elección:

#Onomatopopih debe hacer git push en la terminal
#Onomatopopih debe hacer git pull en la terminal
#Onomatopopih debe hacer git clone git@github.com:Fundamentos/onomatopopih.git en la terminal 'X'

#Onomatopopih se tiene que clonar esa nueva version del repo y luego agregarle el sus aportes asi no se rompe