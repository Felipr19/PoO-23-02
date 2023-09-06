from random import *
from instrumentos import *
from musicos import *


class Banda:

    def __init__(self) -> None:
        self.musicos=[]
        self.instrumentos=[]

    def agregar_musicos(self):
        for i in range(randint(0,5)):
            self.musicos.append(Musico(i))
    
    def agregar_instrumentos(self):
        for _ in self.musicos:
            self.instrumentos.append(choice(Instrumentos))

    def afinar_instrumentos(self):
        for i in range(len(self.musicos)):
            print(self.musicos[i].mostrar_musico() + self.instrumentos[i].afinar_instrumento())


    def tocar(self):
        for i in range(len(self.musicos)):
            print(self.musicos[i].mostrar_musico() + self.instrumentos[i].tocar_instrumento())
