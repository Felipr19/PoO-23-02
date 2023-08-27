#39. Escribir un programa que escriba los números comprendidos entre 1 y 1000. El programa 
#escribirá en la pantalla los números en grupos de 20, solicitando al usuario si quiere o no continuar visualizando el siguiente grupo de números.
n=0
num=0
for i in range(1000):
    num+=1
    if n<20:
        print( f"{num}, ", end="")
        n+=1
    else:
        print("quieres ver mas? si=1/no=0")
        op=int(input())
        if op==1:
            n=0
            num-=1
        elif op==0:
            break