from banda_aleatoria import *

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