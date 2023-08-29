def bubble_sort(arreglo):

    for i in range(len(arreglo)-1):
        for j in range(len(arreglo)-1):
            if arreglo[j]>arreglo[j+1]:
                temp=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=temp
            print(arreglo)
            