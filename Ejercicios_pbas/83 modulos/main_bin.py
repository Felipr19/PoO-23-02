from operaciones_bin import *

b1=int(input("numero binario 1?"))
b2=int(input("numero binario 2?"))

print(f"Que operacion deseas realizar?: \n1.suma \n2.resta \n3.multiplicacion \n4.division")

a=int(input())

if a==1:
    print(suma(b1,b2))
elif a==2:
    print(resta(b1,b2))
elif a==3:
    print(multiplicacion(b1,b2))
elif a == 4:
    print(division(b1,b2))
else:
    print("Esa opcion no es valida")