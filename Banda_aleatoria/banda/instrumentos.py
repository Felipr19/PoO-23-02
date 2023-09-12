from tkinter import PhotoImage
class Instrumento:
    def __init__(self) -> None:
        pass

    def tocar_instrumento(self):
        return(f" esta tocando {self.nombre}")

    
    def afinar_instrumento(self):
        pass 


class Guitarra(Instrumento):
    def __init__(self):
        self.nombre = "la guitarra"


    def afinar_instrumento(self):
        return(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):
    def __init__(self):
        self.nombre = "el piano"


    def afinar_instrumento(self):
        return(" afinó el piano")

class Bateria(Instrumento):

    def __init__(self):
        self.nombre = "la bateria"


    def afinar_instrumento(self):
        return(" afinó las cajas de la bateria")

class Bajo(Instrumento):

    def __init__(self):
        self.nombre = "el bajo"

    def afinar_instrumento(self):
        return(" afinó las cuerdas de el bajo")
    
class Maracas(Instrumento):

    def __init__(self):
        self.nombre = "las maracas"


    def afinar_instrumento(self):
        return(" las maracas no se afinan") 