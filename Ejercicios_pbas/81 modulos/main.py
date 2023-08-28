from operaciones import *
n1=int(input("numero 1?"))
n2=int(input("numero 2?"))

print(f"Que operacion deseas realizar?: \n1.suma \n2.resta \n3.multiplicacion \n4.division \n5.potencia")

a=int(input())

if a==1:
    print(suma(n1,n2))
elif a==2:
    print(resta(n1,n2))
elif a==3:
    print(multiplicacion(n1,n2))
elif a == 4:
    print(division(n1,n2))
elif a == 5:
    print(potencia(n1,n2))
else:
    print("Esa opcion no es valida")