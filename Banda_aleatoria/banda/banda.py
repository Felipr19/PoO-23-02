from random import *
from instrumentos import *
from musicos import *


class Banda:

    def __init__(self):
        self.musicos=[]
        self.instrumentos=[Guitarra(), Piano(), Bajo(), Maracas(), Bateria()]

    def agregar_musicos(self):
        for i in range(randint(1,4)):
            self.musicos.append(Musico(i+1,choice(self.instrumentos)))
    

    def afinar_instrumentos(self):
        for musico in self.musicos:
            print(musico.mostrar_musico() + musico.afinar_instrumento())


    def tocar(self):
        
        for musico in self.musicos:
            print(musico.mostrar_musico() + musico.tocar_instrumento())