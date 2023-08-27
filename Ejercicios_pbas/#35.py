#Escribir un programa que calcule el factorial de un número.
n=int(input())
factorial=1

while n>1:
    factorial=factorial*n
    n-=1

print(factorial)
