class Felino:
    def __init__(self, energia, dormir):
        self.energia = energia
        self.dormir = dormir
    def comer(self, gramos):
        self.energia += gramos * 0.1
    def jugar(self, minutos):
        self.energia -= (minutos // 30) * 10
    def saber_hora(self, horario):
        if 11 <= horario <= 19:
            self.dormir = True
        else:
            self.dormir = False

class Chita(Felino):
    def correr(self, metros):
        self.energia -= (metros // 100) * 30
    def comer(self, gramos):
        self.energia += gramos * 0.2