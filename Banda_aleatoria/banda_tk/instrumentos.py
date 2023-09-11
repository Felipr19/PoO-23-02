from tkinter import PhotoImage
class Instrumento:
    def __init__(self) -> None:
        pass

    def tocar_instrumento(self):
        pass

    
    def afinar_instrumento(self):
        pass 


class Guitarra(Instrumento):
    def __init__(self):
        self.image = "guitar_image.png"

    def tocar_instrumento(self):
        return(" esta tocando la guitarra")

    def afinar_instrumento(self):
        return(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):
    def __init__(self):
        self.image = "piano_image.png"

    def tocar_instrumento(self):
        return(" esta tocando el piano")

    def afinar_instrumento(self):
        return(" afinó el piano")

class Bateria(Instrumento):

    def __init__(self):
        self.image = "bateria_image.png"

    def tocar_instrumento(self):
        return(" esta tocando la bateria")

    def afinar_instrumento(self):
        return(" afinó las cajas de la bateria")

class Bajo(Instrumento):

    def __init__(self):
        self.image = "bajo_image.png"


    def tocar_instrumento(self):
        return(" esta tocando el bajo")

    def afinar_instrumento(self):
        return(" afinó las cuerdas de el bajo")
    
class Maracas(Instrumento):

    def __init__(self):
        self.image = "maracas_image.png"

    def tocar_instrumento(self):
        return(" esta tocando las maracas")

    def afinar_instrumento(self):
        return(" las maracas no se afinan") 

