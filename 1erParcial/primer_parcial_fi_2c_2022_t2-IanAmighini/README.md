# FI_1P_2022_1C_T2
La entrega del examen se hará por este medio: tendrás que confeccionar el código adecuado para realizar cada actividad, generar los archivos correspondientes en el caso de ser necesario y pushearlos a este repo que se te generó automáticamente. 

Las devoluciones de este examen se harán por GitHub Classroom, por medio de Issues y comentarios. **Debés empujar los cambios al repositorio remoto (siguiendo correctamente los pasos) cada 5 min, de lo contrario tu entrega no será considerada válida.**    

### Consigna N°1
Escribir funciones que, dado un String, permitan resolver lo siguiente:

a) Obtener a lista de los substrings delimitados entre '<' y '> que tengan menos de 10 caracteres

b) Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'. Revisá su código propuesto y respondé:

- ¿Qué error/es tiene? (justificá tu respuesta)
- Reescribir el código para que funcione correctamente.

```python
def entre_picos_sin_ab(string):
    return re.findall("X(.^ab*.)Y", a)
```

### Consigna N°2

A) Escribí un programa (función) que reconstruya la frase, extrayéndola de los archivos con extensión `.txt` que se encuentran en el directorio `recursos`, y la escriba en un archivo con el nombre de la escritora, que debés leer del `archivo_5.txt`. NO se pueden usar rutas absolutas y debés hacer la lectura y escritura de archivos de forma automatizada usando las bibliotecas glob y os.

B) Ejecutá el script_misterioso.py y realizá resolvé: 
  1. ¿Qué tipo de exepción arroja la corrida del script? 
  2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error
  3. ¿Qué otras excepciones deberias considerar?


### Consigna N°3

Existen muchos tipos de felinos, los cuales se caracterizan por tener un comportamiento muy similar, más allá de las diferencias que puedan tener en cuanto a tamaño o hábitat. Con esto en mente se propone modelar la clase Felino, la cual tiene como característica su energía y si requiere dormir o no. Además debe entender los mensajes: **comer**, que aumenta su energía en 0.1 puntos por cada gramo que ingiere, **jugar(minutos)** que disminuye su energía 10 puntos por cada media hora de juego y **saber_hora(horario)**, el cual, si la hora está entre las 11 y las 19, el felino duerme.

Los chitas, si bien tienen un comportamiento similar, también hacen cosas particulares. Por ejemplo, pueden correr muy rápido, lo que gasta muy rápido su energía (30 puntos cada 100 metros), sin embargo al comer recuperan el doble de energía que los felinos normales.

Definí las clases Felino y Chita, hacé que esta última herede de la primera, agregando y/o redefiniendo los métodos necesarios. 

### Consigna N°4


Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:

```python
class JuegoDelHambre:
    def __init__(self, poblacion, participantes = []):
        self.poblacion = poblacion
        self.participantes = participantes

    def get_poblacion(self):
        return self.poblacion

    def get_participantes(self):
        return self.participantes
```

a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un objeto de esta clase? ¿Qué mensajes entiende?

b) Instanciá al JuegoDelHambre distrito_13, que tiene como poblacion a `['Peeta', 'Katniss', 'Haymitch']`

c) Definir el método `sortear_participante` que borra un elemento de la poblacion y lo agrega a la lista de participantes

d) Definir un método `avistar_bengala` que borra un elemento de la lista de participantes y devuelve el mensaje `'sinsajo'`


### Consigna N°5

En el equipo de trabajo de Onomatopopih tienen un repositorio compartido para resolver el tp final de la materia de Fundamentos de Informática. Topa hizo un commit inicial con un README con los nombres de los miembros del equipo. Ahora Onomatopopih quiere **descargar** los cambios y hacer su aporte:

```python
def agregador_de_estudiantes(nombre, apellido):
       with open(nombre, 'w') as mi_archivo:
               mi_archivo.readlines()
```

Marcá la/s opcion/es correcta/s. Justificá tu elección: 

* El procedimiento de Onomatopopih al ser invocado genera un error del tipo `UnsupportedOperation`.
* El procedimiento de Onomatopopih al ser invocado genera un error del tipo `SyntaxError`.
* Onomatopopih debe escribir en la terminal `push` al repositorio para compartir los cambios con el equipo.
* Onomatopopih debe escribir en la terminal `pull` del repositorio para compartir los cambios con el equipo.
* Onomatopopih debe escribir en la terminal `git push` al repositorio para compartir los cambios con el equipo.
* Onomatopopih debe escribir en la terminal `git pull` para descargar los cambios que hizo el equipo.
* Onomatopopih para agregar su aporte debe escribir en una terminal `add` y luego `commit`.
* Onomatopopih para agregar su aporte debe escribir en una terminal `git add .`, luego `git commit -m` con el mensaje adecuado para el commit y finalmente `git push`.
