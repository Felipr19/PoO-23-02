class Instrumento:
    def __init__(self) -> None:
        pass

    def tocar_instrumento(self):
        pass

    
    def afinar_instrumento(self):
        pass 

class Guitarra(Instrumento):

    def tocar_instrumento(self):
        return(" esta tocando la guitarra")

    def afinar_instrumento(self):
        return(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):

    def tocar_instrumento(self):
        return(" esta tocando el piano")

    def afinar_instrumento(self):
        return(" afinó el piano")

class Bateria(Instrumento):

    def tocar_instrumento(self):
        return(" esta tocando la bateria")

    def afinar_instrumento(self):
        return(" afinó las cajas de la bateria")

class Bajo(Instrumento):

    def tocar_instrumento(self):
        return(" esta tocando el bajo")

    def afinar_instrumento(self):
        return(" afinó las cuerdas de el bajo")

Instrumentos=[Guitarra(),Piano(),Bajo(),Bateria()]