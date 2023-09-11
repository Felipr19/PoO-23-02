from contador_decimal import ContadorDecimal
from contador_base import ContadorBase



def display_menu():
    print("1: Decimal\n 2: Otro")
    r = int(input("Ingrese el numero de opción segun su tipo de numero: "))
    n = int(input("Ingrese el numero: "))
    contador = None

    if r == 1:
        contador = ContadorDecimal()
        contador.avanza_decimal(n)
        
    elif r == 2:
        o = int(input("Digite la base del numero"))
        contador = ContadorBase()
        contador.avanza_base(n, o)

    else:
        print("El numero ingresado no corresponde con alguna opción del menú")

if __name__ == "__main__":
    display_menu()