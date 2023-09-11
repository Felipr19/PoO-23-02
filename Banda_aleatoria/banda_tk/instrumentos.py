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
        self.image = "guitar_image.png"


    def afinar_instrumento(self):
        return(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):
    def __init__(self):
        self.nombre = "el piano"
        self.image = "piano_image.png"


    def afinar_instrumento(self):
        return(" afinó el piano")

class Bateria(Instrumento):

    def __init__(self):
        self.nombre = "la bateria"
        self.image = "bateria_image.png"


    def afinar_instrumento(self):
        return(" afinó las cajas de la bateria")

class Bajo(Instrumento):

    def __init__(self):
        self.nombre = "el bajo"
        self.image = "bajo_image.png"

    def afinar_instrumento(self):
        return(" afinó las cuerdas de el bajo")
    
class Maracas(Instrumento):

    def __init__(self):
        self.nombre = "las maracas"
        self.image = "maracas_image.png"


    def afinar_instrumento(self):
        return(" las maracas no se afinan") 