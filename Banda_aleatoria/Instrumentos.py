class Instrumento:

    def tocar_instrumento(self):
        pass

    
    def afinar_instrumento(self):
        pass    

class Guitarra(Instrumento):

    def tocar_instrumento(self):
        print(" esta tocando la guitarra")

    def afinar_instrumento(self):
        print(" afinó las cuerdas de la guitarra")

class Piano(Instrumento):

    def tocar_instrumento(self):
        print(" esta tocando el piano")

    def afinar_instrumento(self):
        print(" afinó el piano")

class Bateria(Instrumento):

    def tocar_instrumento(self):
        print(" esta tocando la bateria")

    def afinar_instrumento(self):
        print(" afinó la bateria")

class Bajo(Instrumento):

    def tocar_instrumento(self):
        print(" esta tocando el bajo")
    
    def afinar_instrumento(self):
        print(" afinó el bajo")