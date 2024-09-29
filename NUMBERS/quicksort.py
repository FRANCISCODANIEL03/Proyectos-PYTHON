"""
Ordenamiento quicksort
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr)//2]
    izq = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    der = [x for x in arr if x > pivote]

    return quick_sort(izq) + quick_sort(centro) + quick_sort(der)

array = [1,4,6,45,67,3,23,12]
print(array)
print(quick_sort(array))

"""
Existe una excepcion con este metodo:
    * Si se excede el limite de recursividad no funcionara
"""