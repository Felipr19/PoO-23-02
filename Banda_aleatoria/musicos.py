from instrumentos import *

class Musico:

    def __init__(self,numero) -> None:
        self.numero=numero

    def mostrar_musico(self):
        return(f"Musico {self.numero}")