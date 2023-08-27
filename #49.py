#Escribir un programa que determine la posición de una matriz de 3x3 en la que se encuentra el valor máximo de una serie de números generados aleatoriamente
from random import randint
mt=[[1,2,3],[4,5,6],[7,8,9]]
mtrz=[[randint(0,99),randint(0,99),randint(0,99)],
      [randint(0,99),randint(0,99),randint(0,99)],
      [randint(0,99),randint(0,99),randint(0,99)]]
max=0
for i in range(len(mtrz)):
    for j in range(len(mtrz)):
        print(f"{mtrz[i][j]} ,",end="")
        if mtrz[i][j]>max:
            max=mtrz[i][j]
            a=i
            b=j
    print("")

print(f"el valor max es {max} y esta en la pos {a},{b}")