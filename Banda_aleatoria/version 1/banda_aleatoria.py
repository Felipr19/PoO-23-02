from musico import *
from instrumento import *
from random import choice
from random import randint

class BandaAleatoria(Instrumento):

    def crear_banda(self):
        self.integrantes = dict()
        for i in range(randint(1, len(self.lista_musicos)+1)):
            musico_aleatorio = choice(self.lista_musicos)
            instrumento_aleatorio = choice(self.lista_instrumentos)
            self.integrantes[musico_aleatorio] = instrumento_aleatorio

        for nombre_edad, instrumento in zip(self.integrantes.keys(), self.integrantes.values()):
            print(nombre_edad[0], nombre_edad[1], instrumento)

        return self.integrantes

    lista_musicos = list() #Why to use in here? and not inside?
    def cargar_musico(self, musico):
        self.lista_musicos.append(musico)

    lista_instrumentos = list()
    def cargar_instrumento(self, instrumento):

        self.lista_instrumentos.append(instrumento)
        #Piano.afinar_instrumento(self)


    


if __name__ == "__main__":
    banda_1 = BandaAleatoria()
    musico_1 = Musico("Jorge", "26")
    musico_2 = Musico("Andres", "28")

    banda_1.cargar_musico(tuple((musico_1.nombre, musico_1.edad)))
    banda_1.cargar_musico(tuple((musico_2.nombre, musico_2.edad)))

    banda_1.cargar_instrumento("Piano")
    banda_1.cargar_instrumento("Guitarra")
    banda_1.cargar_instrumento("Bateria")
    banda_1.cargar_instrumento("Flauta")
    banda_1.cargar_instrumento("Bajo")

    print(banda_1.lista_instrumentos)
    print(banda_1.crear_banda())
    print(banda_1.lista_musicos)

    