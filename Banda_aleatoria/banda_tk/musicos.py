from instrumentos import *

class Musico:

    def __init__(self,numero,Instrumento):
        self.numero=numero
        self.instrumento=Instrumento

    def mostrar_musico(self):
        return(f"Musico {self.numero}")
    
    def tocar_instrumento(self):
        return self.instrumento.tocar_instrumento()

    def afinar_instrumento(self):
        return self.instrumento.afinar_instrumento()