# Simulacro Primer Parcial
La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso de ser necesario y pushearlos a este repo que se te generó automáticamente. 

Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. **Debés hacer un push (siguiendo correctamente los pasos) cada 5 min, de lo contrario tu entrega no será considerada válida.**   

### Consigna N°1
Escribir funciones que, dado un String, permitan:

a) Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'. Por ejemplo para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].

b) Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer la lista de substrings delimitadas por los patrones 'ag' y 'cta', no incluyan números. Revisá su código propuesto y marcá con una `x` las opciones correctas. JUSTIFICA tus respuestas.

```python
def funcionDeExpresiones_Regulares():
    return re.findal("ag(\d.*?)cta")
```

- El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python
- La función devuelve NameError al ser ejecutada
- La función devuelve SintaxError al ser ejecutada
- Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['gaaa']
- Una vez corregida la función, cuando se la invoca usando el texto 'aabocaggaaactazu4lggaasag24gra1ndecta' devuelve ['24gra1nde']


### Consigna N°2

A) En la agencia SIDRA (Somos Inteligentes por Demás y Rara vez Alardeamos) tienen agentes secretos dieseminados por el mundo. El medio de contacto con los agentes es por correo electrónico, mediante cuentas con identidades falsas. La agencia nos facilitó dos archivos secretos que contienen escondidas las cuentas de los agentes para que los ayudemos a construir un programa que lea los archivos `.txt` y extraiga todas las cuentas de gmail de los agentes secretos y las almacene en un único archivo `base_de_datos.txt` . Usá todo lo que sabes de las bibliotecas `os`, `glob` y `re`

B) Ejecutá el script_misterioso.py y realizá resolvé:

  i. ¿Qué tipo de exepción arroja la corrida del script?

  ii. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 3. ¿Qué otras excepciones deberias considerar?



### Consigna N°3

Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:

```python
class EntrenadorPokemon():
   def __init__(self, batallas_ganadas = 0, lista_pokemons = []):
      self.batallas_ganadas = batallas_ganadas
      self.pokemons = lista_pokemons
   
   def get_batallas_ganadas(self):
      return self.batallas_ganadas

   def get_pokemons(self):
      return self.pokemons
```

a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un objeto de esta clase? ¿Qué mensajes entiende?

b) Instanciá al EntrenadorPokemon Ash, que tiene 25 batallas_ganadas y a `pikachu` entre sus pokemons. 

c) Definir el método agregar_pokemon que incorpora un pokemon a la lista de pokemons que tiene un EntrenadorPokemon en su equipo.

d) Definir un método perder_batalla que descuenta 1 de las batallas_ganadas y elimina un pokemon de la lista de pokemons.


### Consigna N°4

**A)** Vamos a modelar de manera muy simple la mecánica de un nuevo juego de Pac-Man con algunas modificaciones al original. Consideremos tanto los puntos que obtiene comiendo bolitas como los puntos que obtiene al comerse a los fantasmas, sin embargo en este nuevo juego cada fantasma otorga distinta cantidad de puntos, siendo el rosa el que mayor puntaje da (8 puntos), seguido del verde (6), el naranja (4) y el rojo (2). Además mientras más puntos tiene, más rápido se va a mover. Como en todo juego de Pac-Man, si lo toca un fantasma se pierde una vida y si se queda sin vidas se termina el juego; inicialmente Pac-Man tiene 3 vidas. Dicho todo esto Pac-Man debe entender los siguientes mensajes:

- **comerBolita(cantidad)** el cual aumenta el puntaje esta cantidad multiplicada por 2.
- **velocidad()**, que nos dice cuánta velocidad va a tener Pac-Man en ese período de tiempo. La fórmula sería: velocidad = 2 + puntos / 100
- **perderVida** lo que provoca que disminuya en 1 el contador de vidas y resetea el puntaje de bolitas. Si llega a 0 tiene que aparecer un cartel de "Game Over".
- **comer(fantasma)**, el cual va a aumentar el puntaje dependiendo de qué color era el fastasma que comió.

Definí la clase **PacMan**, instanciala y luego ejecutá:

```python
pacman.comerBolita(22)
pacman.perderVida()
pacman.comerFantasma("Rojo")
pacman.comerFantasma("Rosa")
print(pacman.puntos)
pacman.comerBolita(20)
print(pacman.velocidad())
pacman.perderVida()
pacman.perderVida()
```

El resultado de esto debería ser:

	10
    2.5
    GAME OVER

**B)** A medida que avanza el juego Pac-Man obtiene nuevas habilidades tales como ganar una vida extra si llega a 200 puntos, restando esta cantidad de puntos al puntaje y además ahora gana más velocidad a medida que suma puntos de la forma: velocidad = 3 + puntos / 100. Definí la clase **PacManMejorado** que herede de **PacMan**, pero que además entienda **vidaExtra()**, el cual debe comprobar si se cumple con la condición y aumentar en 1 la cantidad de vida y en caso contrario debe aparecer un cartel indicando cuántos puntos le faltan para conseguir una nueva vida. También se tiene que redefinir el método **velocidad()** para que cumpla con lo indicado.
Ejecutando las siguientes líneas (eliminando la ejecución del inciso **A**):

```python
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
```

El resultado de esto debería ser:
	
	10
    4.7
    2
    3
    Faltan 170 puntos para ganar una vida extra
    GAME OVER

### Consigna N°5

En el equipo de trabajo de Onomatopopih tienen un repositorio compartido para resolver el tp final de la materia de Fundamentos de Informática. Topa hizo un commit inicial con un README con los nombres de los miembros del equipo. Ahora Onomatopopih quiere descargar los cambios para hacer su aporte. 

A) Marcá con una [X] la/s opcion/es correcta/s y justifica tu elección:

- Onomatopopih debe hacer `push` en la terminal 
- Onomatopopih debe hacer `pull` en la terminal 
- Onomatopopih debe hacer `git push` en la terminal
- Onomatopopih debe hacer `git pull` en la terminal
- Onomatopopih después de agregar su aporte debe escribir en una terminal `git add` y luego `git commit`
- Onomatopopih después de agregar su aporte debe escribir en una terminal `git add .`, luego `git commit -m 'mis aportes'` y finalmente `git push`

Al tiempo, Onomatopopih descubrió que sus compañeros actualizaron elrepositorio. Marcá con una [X] la/s opcion/es correcta/s y justifica tu elección: 

- Onomatopopih debe hacer `git push` en la terminal 
- Onomatopopih debe hacer `git pull` en la terminal 
- Onomatopopih debe hacer `git clone git@github.com:Fundamentos/onomatopopih.git` en la terminal 
