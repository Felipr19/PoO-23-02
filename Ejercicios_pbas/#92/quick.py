def quick_sort(arreglo, low, high):
    if low < high:
        pi = particion(arreglo, low, high)
  
        quick_sort(arreglo, low, pi - 1)
        quick_sort(arreglo, pi + 1, high)
 
def particion(arreglo, low, high):  
  
    pivot = arreglo[high]
  
  
    i = low - 1
 
    for j in range(low, high):
        if arreglo[j] <= pivot:
            i+=1
            (arreglo[i], arreglo[j]) = (arreglo[j], arreglo[i])
        print(arreglo)

    (arreglo[i + 1], arreglo[high]) = (arreglo[high], arreglo[i + 1])
  
    return i + 1