from random import *
from instrumentos import *
from musicos import *
from tkinter_banda import *

class Banda:

    def __init__(self):
        self.musicos=[]
        self.instrumentos=[Guitarra(), Piano(), Bajo(), Maracas(), Bateria()]

    def agregar_musicos(self):
        for i in range(randint(1,4)):
            self.musicos.append(Musico(i,choice(self.instrumentos)))
    

    def afinar_instrumentos(self):
        for musico in self.musicos:
            print(musico.mostrar_musico() + musico.afinar_instrumento())


    def tocar(self):
        instrumentos_img=[]
        for musico in self.musicos:
            instrumentos_img.append(musico.instrumento.image)
            print(musico.mostrar_musico() + musico.tocar_instrumento())
        activate_photo(instrumentos_img)