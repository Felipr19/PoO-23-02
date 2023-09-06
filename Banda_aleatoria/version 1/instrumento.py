class Instrumento:
    lista_instrumentos = []

    def afinar_instrumento(self):
        pass

    def cargar_instrumento(self):
        pass

class Guitarra(Instrumento):

    def afinar_instrumento(self):
        return "Afinando guitarra"
    
class Bajo(Instrumento):

    def afinar_instrumento(self):
        return "Afinando bajo"
    
class Flauta(Instrumento):

    def afinar_instrumento(self):
        return "Afinando flauta"
    
class Piano(Instrumento):
    def afinar_instrumento(self):
        return "Afinando piano"
    
class Bateria(Instrumento):
    def afinar_instrumento(self):
        return "Afinando bateria"
    

    
