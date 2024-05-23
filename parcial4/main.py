import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, nombre):
        #se inicializa un nodo para el arbol genealogico con el nombre ingresado
        self.nombre = nombre
        self.padre = None
        self.madre = None
        self.hijos = []

class ArbolGenealogico:
    def __init__(self):
        #se inicializa con un diccionario vacio de miembros y niveles
        self.miembros = {}
        self.niveles = {}

    def agregar_miembro(self, nombre, edad):
        #Agregamos un miembro al arbol con el nombre entrado por parametro
        if nombre not in self.miembros:
            self.miembros[nombre] = Nodo(nombre)
            
    def agregar_relacion_padre_hijo(self, nombre_padre, nombre_hijo):
        #Se establece la relacion padre hijo entre dos miembros del arbol
        #se verifica si el padre y el hijo existen y ubica los nodos correspondientes con su relacion
        #se actualiza los niveles del arbol ya que al agregar un hijo la estructura puede cambiar
        if nombre_padre in self.miembros and nombre_hijo in self.miembros:
            padre = self.miembros[nombre_padre]
            hijo = self.miembros[nombre_hijo]
            if hijo not in padre.hijos:
                padre.hijos.append(hijo)
                if hijo.padre is None:
                    hijo.padre = padre
                else:
                    hijo.madre = padre
            self.asignar_niveles()

    def asignar_niveles(self):
        #Se le asignan los niveles a cada miembro del arbol
        #Llama a la función interna asignar_niveles_recursivo para asignar niveles a cada nodo.
        def asignar_niveles_recursivo(raiz, nivel):
            if raiz:
                self.niveles[raiz.nombre] = nivel
                for hijo in raiz.hijos:
                    asignar_niveles_recursivo(hijo, nivel + 1)
        
        # Encuentra las raíces del árbol (nodos sin padres) es decir el más antiguos de la familia
        raices = [nodo for nodo in self.miembros.values() if nodo.padre is None and nodo.madre is None]
        for raiz in raices:
            asignar_niveles_recursivo(raiz, 0)

    def imprimir_arbol(self):
        #imprimr el arbol con informacion de: padre,hijos,hermanos,nietos...
        if not self.miembros:
            print("El árbol está vacío.")
        else:
            print("Árbol Genealógico:")
            for nombre, persona in self.miembros.items():
                print(f"Nombre: {nombre}")
                #obtiene el nombre del padre y la madre del nodo
                print("Padres:")
                if persona.padre:
                    print(f"- {persona.padre.nombre}")
                if persona.madre:
                    print(f"- {persona.madre.nombre}")
                #obtiene el nombre de los hijos del nodo
                print("Hijos:")
                for hijo in persona.hijos:
                    print(f"- {hijo.nombre}")
                print("Hermanos:")
                #obtiene el nombre de los hermanos del nodo
                if persona.padre:
                    hermanos = [h.nombre for h in persona.padre.hijos if h.nombre != nombre]
                    print(", ".join(hermanos) if hermanos else "Ninguno")
                print("Nietos:")
                for hijo in persona.hijos:
                    # Obtener los nombres de los nietos del nodo
                    nietos = [n.nombre for n in hijo.hijos]
                    print(f"- {hijo.nombre}: {', '.join(nietos) if nietos else 'Ninguno'}")
                print()
                
    def get_ancestros(self, nombre):
        if nombre in self.miembros:
            persona = self.miembros[nombre]
            ancestros = set()

            # Verificar si la persona tiene padre y madre
            if persona.padre:
                ancestros.add(persona.padre.nombre)
                ancestros.update(self.get_ancestros(persona.padre.nombre))
            if persona.madre:
                ancestros.add(persona.madre.nombre)
                ancestros.update(self.get_ancestros(persona.madre.nombre))
            return ancestros
        return set()


    def encontrar_ancestro_comun(self, nombre1, nombre2):
        if nombre1 in self.miembros and nombre2 in self.miembros:
            ancestros1 = self.get_ancestros(nombre1)
            ancestros2 = self.get_ancestros(nombre2)

            # Verificar si uno de los miembros no tiene ancestros
            if not ancestros1 or not ancestros2:
                return None

            comun = ancestros1.intersection(ancestros2)
            if comun:
                return comun
        return None



    def determinar_relacion(self, nombre1, nombre2):
        #se encuentra el parentesco entre dos miembros del arbol
        #de acuerdo a la diferencia de sus alturas en el arbol
        if nombre1 in self.miembros and nombre2 in self.miembros:
            nivel1 = self.niveles.get(nombre1, -1)
            nivel2 = self.niveles.get(nombre2, -1)
            diferencia = abs(nivel1 - nivel2)

            if diferencia == 0:
                return f"{nombre1} y {nombre2} son hermanos"
            elif diferencia == 1:
                if nivel1 < nivel2:
                    return f"{nombre1} es padre/madre de {nombre2}"
                else:
                    return f"{nombre1} es hijo/a de {nombre2}"
            elif diferencia == 2:
                if nivel1 < nivel2:
                    return f"{nombre1} es abuelo/abuela de {nombre2}"
                else:
                    return f"{nombre1} es nieto/a de {nombre2}"
            else:
                return "Relación más lejana"
        return "Uno o ambos miembros no existen en el árbol"

    def graficar_arbol(self):
        #Grafica el árbol genealógico utilizando NetworkX y Matplotlib
        G = nx.DiGraph()
        for nombre, persona in self.miembros.items():
            G.add_node(persona.nombre)
            for hijo in persona.hijos:
                G.add_edge(persona.nombre, hijo.nombre)

        plt.figure(figsize=(10, 6))  
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold")
        plt.title("Árbol Genealógico")
        plt.show()  



    def agregar_miembro_con_relaciones(self, nombre, edad, padres=[], hijos=[]):
        #se agrega un nuevo miembro con las relaciones de padre_hijos definidas arriba
        self.agregar_miembro(nombre, edad)
        for padre in padres:
            self.agregar_miembro(padre, 0)
            self.agregar_relacion_padre_hijo(padre, nombre)
        for hijo in hijos:
            self.agregar_miembro(hijo, 0)
            self.agregar_relacion_padre_hijo(nombre, hijo)

def menu():
    familia = ArbolGenealogico()
    # Agrego miembros a la familia
    familia.agregar_miembro("Roberto", 70)
    familia.agregar_miembro("Juan", 50)
    familia.agregar_miembro("Carlos", 30)
    familia.agregar_miembro("Pedro", 25)
    familia.agregar_miembro("Maria", 20)
    familia.agregar_miembro("Luisa", 18)

    # Establezco relaciones padre-hijo
    familia.agregar_relacion_padre_hijo("Roberto", "Juan")
    familia.agregar_relacion_padre_hijo("Juan", "Carlos")
    familia.agregar_relacion_padre_hijo("Juan", "Pedro")
    familia.agregar_relacion_padre_hijo("Juan", "Maria")
    familia.agregar_relacion_padre_hijo("Juan", "Luisa")

    # Asigno niveles iniciales
    familia.asignar_niveles()

    while True:
        print("\nOpciones:")
        print("1. Agregar miembro con relaciones")
        print("2. Imprimir árbol genealógico")
        print("3. Graficar árbol genealógico")
        print("4. Encontrar ancestro en común ")
        print("5. Determinar parentesco entre dos miembros")
        print("6. salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del nuevo miembro: ")
            edad = int(input("Edad del nuevo miembro: "))
            padres = input("Nombres de los padres (separados por comas, si no tiene, dejar vacío): ").split(",")
            hijos = input("Nombres de los hijos (separados por comas, si no tiene, dejar vacío): ").split(",")
            padres = [p.strip() for p in padres if p.strip()]
            hijos = [h.strip() for h in hijos if h.strip()]
            familia.agregar_miembro_con_relaciones(nombre, edad, padres, hijos)
        elif opcion == "2":
            familia.imprimir_arbol()
        elif opcion == "3":
            familia.graficar_arbol()
        elif opcion == "4":
            nombre1 = input("Ingrese el nombre del primer miembro: ")
            nombre2 = input("Ingrese el nombre del segundo miembro: ")
            ancestro_comun = familia.encontrar_ancestro_comun(nombre1, nombre2)
            if ancestro_comun:
                print(f"El ancestro común más reciente entre {nombre1} y {nombre2} es: {', '.join(ancestro_comun)}")
            else:
                print(f"No hay ancestro común entre {nombre1} y {nombre2}.")
        elif opcion == "5":
            nombre1 = input("Ingrese el nombre del primer miembro: ")
            nombre2 = input("Ingrese el nombre del segundo miembro: ")
            parentesco = familia.determinar_relacion(nombre1, nombre2)
            print(parentesco)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()