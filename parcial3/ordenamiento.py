import random #se utiliza para generar números aleatorios
import time # para medir el tiempo de ejecución
import matplotlib.pyplot as plt #para  gráficos.



def generar_lista_aleatoria(tamano): #Genera una lista aleatoria del tamaño ingresado por parametro
    lista_aleatoria = [random.randint(0, 1000) for _ in range(tamano)]
    return lista_aleatoria


def imprimir_lista(list): # imprime los elementos de la lista.
    for num in list:
        print(num)



def selection_sort(list): #itera sobre la lista y busca el elemento mas pequeño desde una posicion hasta el final de la lista. Luego intercambia este elemento pqueño con el otro elemento.hasta que la lista este  ordenada.
    n= len(list) #longitud de la lista.

    for i in range(n-1):
        minpos= i #se pone posición inicial como el más pequeño.
        for j in range(i + 1, n): #itera en busca del elemento mas pequeño
            if list[j]<list[minpos]: #se comparan los elementos 
                minpos = j #de encontrar uno mas pequeño se hace el cambio de minpos
        list[i], list[minpos]=list[minpos], list[i] #se hace el intercambio de posiciones
    return list

def bubble_sort(list): # compara parejas de elementos en la lista y los intercambia si estan orden incorrecto.  se repite en la lista hasta que no se hagan intercambios,  Si esata ordenado no se realiza ningún intercambio
    n= len(list)# longitud de la lista.
    swapped= True  # controla si se realizan intercambios o no 
    for i in range(n - 1): #itera sobre la lista desde el primer elemento hasta el último.
        swapped=False
        for j in range(n-i-1):# desde el perimer elemento hasta el ultim no ordenado
            if list[j] > list[j + 1]: #Compara cada elemento si es mayor con su vecino.
                list[j], list[j + 1]= list[j + 1], list[j] #si es mayor se hace el cambio 
                swapped =True
        if not swapped:
            break
    return list

def merge_sort(list): # divide la lista en mitades hasta que cada lista pqueña tenga un solo elemento.luego combina las sublistas en una lista ordenada . se hace hasta que se haya ordenado toda la lista.
    if len(list) > 1: # se verifica si tiene mas de un elemento 
        mid = len(list) // 2 #se calcula la mitad de la lista 
        L= list[:mid] # la divido en dos mitades esta es izquierda
        R= list[mid:]#mitad derecha
        merge_sort(L)#se hace llamada recursiva con cada lado 
        merge_sort(R)
        i = j = k = 0 # se inicializan los contadores
        while i< len(L) and j < len(R): # se combinan las peuqeñas en una sola ordenada

            if L[i]< R[j]: # se comparan los elementos y s epone el mas pequeño en la lista grande
                list[k]= L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):#añaden los restantes 
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
    return list

def insertion_sort(list): # recorre la lista desde el segundo elemento hasta el ultimo.y compara el elemento actual con los elementos anteriores y lo inserta en la posición correcta hasta que la lista este ordenada
    for i in range(1, len(list)):#se recorre desde el segundo hasta el ultimo
        elem= list[i]  #se selecciona el que voy a insertar los elementos anteriores y mueve los elementos mayores hacia la derecha
        j = i- 1 # Inicializa un índice para comparar con los elementos anteriores al elemento actual
        while j >= 0 and elem < list[j]: #Compara el elemento actual con los elementos anteriores 
            list[j + 1] = list[j] # se comparan los anteriores para hacer espacio para el elemento que vamos a insertar
            j -= 1 # se disminuye el indice para comparar con los otros elementos 
            list[j + 1] = elem# se inserta el elemento 
    return list   



if __name__ == "__main__": 
    def main():
        tamanios = [10, 100, 1000, 10000]  # Lista de tamaños del arreglo
        execution_times_selection = []
        execution_times_bubble = []
        execution_times_merge = []
        execution_times_insertion = []

        for tamanio in tamanios: #Itera sobre una lista de tamaños [10, 100, 1000, 10000].

            lista= generar_lista_aleatoria(tamanio) #Para cada tamaño, genera una lista aleatoria.

            print("Ordenamiento por selectionSort:")
            start_time = time.time()  #inicia el tiempo de ejecución 
            selection_sort(lista) #se hace el llamado de la funcion con la lista desordenada
            end_time = time.time() #termina de medir el tiempo de ejecucion 
            execution_time = end_time - start_time
            execution_times_selection.append(execution_time) #almacena el tiempo de ejecución en una lista 
            print(f"Tiempo total de ejecución para tamaño {tamanio}: {execution_time:.6f} segundos")
            #imprimir_lista(lista)

            print("Ordenamiento por BubbleSort:")
            start_time = time.time()  #inicia el tiempo de ejecución 
            bubble_sort(lista) #se hace el llamado de la funcion con la lista desordenada
            end_time = time.time() #termina de medir el tiempo de ejecucion 
            execution_time = end_time - start_time
            execution_times_bubble.append(execution_time) #almacena el tiempo de ejecución en una lista 
            print(f"Tiempo total de ejecución para tamaño {tamanio}: {execution_time:.6f} segundos")
            #imprimir_lista(lista)

            print("Ordenamiento por MergeSort:")
            start_time = time.time()  #inicia el tiempo de ejecución 
            merge_sort(lista)  #se hace el llamado de la funcion con la lista desordenada
            end_time = time.time()  #termina de medir el tiempo de ejecucion 
            execution_time = end_time - start_time
            execution_times_merge.append(execution_time) #almacena el tiempo de ejecución en una lista 
            print(f"Tiempo total de ejecución para tamaño {tamanio}: {execution_time:.6f} segundos")
            #imprimir_lista(lista)

            print("Ordenamiento por InsertSort:")
            start_time = time.time()  #inicia el tiempo de ejecución 
            insertion_sort(lista)  #se hace el llamado de la funcion con la lista desordenada
            end_time = time.time() #termina de medir el tiempo de ejecucion 
            execution_time = end_time - start_time
            execution_times_insertion.append(execution_time)#almacena el tiempo de ejecución en una lista 
            print(f"Tiempo total de ejecución para tamaño {tamanio}: {execution_time:.6f} segundos")
            #imprimir_lista(lista)

        plt.plot(tamanios, execution_times_selection, marker='o', label='SelectionSort') #ingresan los datos de la grafica 
        plt.plot(tamanios, execution_times_bubble, marker='o', label='BubbleSort')
        plt.plot(tamanios, execution_times_merge, marker='o', label='MergeSort')
        plt.plot(tamanios, execution_times_insertion, marker='o', label='InsertSort')
        plt.xlabel('Tamaño del conjunto de datos') #titulos
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.title('Tiempo de ejecución de los algoritmos de ordenamiento')
        plt.yscale('log') 
        plt.xscale('log')
        plt.legend()
        plt.grid(True)
        plt.show()


    main()