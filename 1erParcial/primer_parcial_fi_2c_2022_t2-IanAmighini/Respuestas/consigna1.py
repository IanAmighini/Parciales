import re

#A)
def entre_mayor_menor(string):
    patron = '<(.{,10})>'
    return re.findall(patron, string)

print(entre_mayor_menor('<123456789>sdfsf<11223344556677>'))

#B)
#def entre_picos_sin_ab(string):
#    return re.findall("X(.^ab*.)Y", a)

#Para empezar, el a del final no esta definido, tendria que ser la palabra string lo que va despues de la coma.
#El nombre de la funcion esta mal colocado, la consigna pide que tenga la subsecuencia ab dentro del string y que este delimitado por X e Y.
#El patron tambien esta mal escrito ya que queres tener entre la X y el ab varias cosas y ahi solo le esta pidiendo que encuentre una vez cualquier cosa
#El asterisco despues del ab lo va a buscar 0 o mas veces y nosotros queremos que este en el string

def entre_XY_con_ab(string):
    return re.findall("X(.*?ab.*?)Y", string)

print(entre_XY_con_ab('ccvX234absdfYsjdfXllkkkY'))