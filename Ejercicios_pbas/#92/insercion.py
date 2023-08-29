def inserccion_sort(arreglo):

    for i in range(1,len(arreglo)):
        valor = arreglo[i]
        j = i-1
        while j >= 0 and valor < arreglo[j]:
            arreglo[j+1] = arreglo[j]
            j-=1
        arreglo[j+1] = valor
        print(arreglo)