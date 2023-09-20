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
        self.image = "Images/guitar_image.png"


    def afinar_instrumento(self):
        return(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):
    def __init__(self):
        self.nombre = "el piano"
        self.image = "Images/piano_image.png"


    def afinar_instrumento(self):
        return(" afinó el piano")

class Bateria(Instrumento):

    def __init__(self):
        self.nombre = "la bateria"
        self.image = "Images/bateria_image.png"


    def afinar_instrumento(self):
        return(" afinó las cajas de la bateria")

class Bajo(Instrumento):

    def __init__(self):
        self.nombre = "el bajo"
        self.image = "Images/bajo_image.png"

    def afinar_instrumento(self):
        return(" afinó las cuerdas de el bajo")
    
class Maracas(Instrumento):

    def __init__(self):
        self.nombre = "las maracas"
        self.image = "Images/maracas_image.png"


    def afinar_instrumento(self):
        return(" las maracas no se afinan") 
