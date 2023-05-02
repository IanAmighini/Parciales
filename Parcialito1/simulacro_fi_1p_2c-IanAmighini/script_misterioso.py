try:
  def trasladar(una_lista, otra_lista, elemento):
    otra_lista.append(elemento)
    una_lista.remove(elemento)
  lista = [2,5,8]
  listita = []
  trasladar(listita, lista, 2)  
except ValueError:
  print("El elemento no se encuentra en esa lista")

  #El try deberia de ir justo despues del def