import random

def busqueda_secuencial(list, a):
    n = len(list)
    con = 0
    for i in range(n):
        con += 1
        if a == list[i]:
            print("se ejecuto", con)
            return i
    print("se ejecuto", con)
    return -1

def busqueda_binaria(list, j):
    a = 0
    b = len(list) - 1
    con = 0
    while a <= b:
        con += 1
        i = (a + b) // 2
        if j == list[i]:
            print("se ejecuto", con)
            return i
        elif j < list[i]:
            b = i - 1
        else:
            a = i + 1
    print("se ejecuto", con)
    return -1

def llenar_lista(list):
    n = len(list)
    for i in range(n):
        list[i] = random.randint(0, 1000)

def imprimir_lista(list):
    for num in list:
        print(num)

def copiar_lista(list1, list):
    for i in range(len(list)):
        list1[i] = list[i]

def selection_sort(list):
    n = len(list)
    n_veces = 0
    for i in range(n - 1):
        minpos = i
        for j in range(i + 1, n):
            n_veces += 1
            if list[j] < list[minpos]:
                minpos = j
        list[i], list[minpos] = list[minpos], list[i]
    print("se ejecuto:", n_veces)
    return list

def bubble_sort(list):
    n = len(list)
    n_veces = 0
    swapped = True
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            n_veces += 1
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break
    print("se ejecuto:", n_veces)
    return list

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key




if __name__ == "__main__":
    
    def main():
        n = int(input("Tamaño del lista a crear: "))
        lista = [0] * n
        lista1 = [0] * n  # ordenamiento secuencia

        # llenar el arreglo con números aleatorios de 0 a 1000
        llenar_lista(lista)
        copiar_lista(lista1, lista)  # copia ‘arreglo’ en ‘arreglo1’
        print("Imprimir lista original:")
        imprimir_lista(lista)

        print("Ordenamiento por Selección:")
        selection_sort(lista1)
        print("Imprimir lista ordenado por SelectionSort:")
        imprimir_lista(lista1)

        print("Ordenamiento por MergeSort:")
        merge_sort(lista1)
        print("Imprimir lista ordenado por MergeSort:")
        imprimir_lista(lista1)

        print("Ordenamiento por BubbleSort:")
        bubble_sort(lista1)
        print("Imprimir lista ordenado por BubbleSort:")
        imprimir_lista(lista1)

        print("Ordenamiento por Inserción:")
        insertion_sort(lista1)
        print("Imprimir lista ordenado por Inserción:")
        imprimir_lista(lista1)

        value = int(input("Digite un elemento a buscar: "))
        print("Buscandolo en lista desordenado...")
        found = busqueda_secuencial(lista, value)
        print("Encontrado en índice:", found)
        print("Buscandolo en lista ordenado...")
        found = busqueda_binaria(lista1, value)
        print("Encontrado en índice:", found)
    main()
