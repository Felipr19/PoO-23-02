#Escribir un programa que llene una lista con los veinte primeros números pares y calcule su suma. 
pares=[]
for i in range(1,21):
    pares.append(i*2)

print(sum(pares))