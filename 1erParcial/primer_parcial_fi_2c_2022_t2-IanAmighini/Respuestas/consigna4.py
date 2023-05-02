class JuegoDelHambre:
    def __init__(self, poblacion, participantes = []):
        self.poblacion = poblacion
        self.participantes = participantes

    def get_poblacion(self):
        return self.poblacion

    def get_participantes(self):
        return self.participantes
    
    def sortear_participante(self):
        self.participantes.append(self.poblacion[0])
        self.poblacion.remove(self.poblacion[0])
    
    def avistar_bengala(self):
        self.participantes.remove(self.participantes[0])
        print('sinsajo')

#A) El nombre de la clase es JuegoDelHambre, el estado es poblacion y participantes, entiende get_poblacion y get_participantes

#B)
distrito_13 = JuegoDelHambre(['Peeta', 'Katniss', 'Haymitch'])


distrito_13.sortear_participante()
distrito_13.sortear_participante()
print(distrito_13.get_participantes())
print(distrito_13.get_poblacion())
distrito_13.avistar_bengala()
print(distrito_13.get_participantes())