import os, glob

def frase():
    os.chdir('../recursos')
    textos = glob.glob('*.txt')
    with open('archivo_5.txt', 'r') as escritora:
        nombre = escritora.read()
        with open(nombre, 'a') as salida:
            for archivo in textos:
                with open(archivo, 'r') as texto:
                    salida.write(texto.read())

frase()