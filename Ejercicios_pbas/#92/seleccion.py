def seleccion_sort(arreglo):
    for i in range( len(arreglo)-1):
        minIDX=i
        
        for j in range(i+1,len(arreglo)):
            if arreglo[j] < arreglo[minIDX]:
                minIDX = j
            
        (arreglo[i], arreglo[minIDX]) = (arreglo[minIDX], arreglo[i])

        print(arreglo)