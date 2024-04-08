import json

class Node:
    def __init__(self,book_id,title,author,parent=None):
        self.book_id=book_id
        self.title=title
        self.author=author
        self._parent=parent
        self.left=None
        self.right=None
        self.height=1 
        self.borrowed = False  # Estado de préstamo del libro
class AVLTree:
    def __init__(self):
        self.root= None

    def insert(self,book_id,title,author):
        if not self.root:
            self.root = Node(book_id,title, author)
        else:
            self._insert(book_id,title,author,self.root)

    def _insert(self,book_id, title,author, current_node):
        if book_id<current_node.book_id:
            if current_node.left:
                self._insert(book_id,title,author,current_node.left)
            else:
                current_node.left=Node(book_id,title,author, current_node)
                self._inspect_insertion(current_node.left)
        elif book_id>current_node.book_id:
            if current_node.right:
                self._insert(book_id,title,author,current_node.right)
            else:
                current_node.right=Node(book_id,title,author,current_node)
                self._inspect_insertion(current_node.right)
        else:
            print("el libro con ID",book_id, "ya esta en el arbol")
    
    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node._parent is None: return
        path = [cur_node] + path

        left_height = self.get_height(cur_node._parent.left)
        right_height = self.get_height(cur_node._parent.right)

        if abs(left_height-right_height) > 1:
            path = [cur_node._parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height 
        if new_height>cur_node._parent.height:
            cur_node._parent.height = new_height

            self._inspect_insertion(cur_node._parent, path)
    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._rotate_right(z)
        elif y == z.left and x == y.right:
            self._rotate_left(y)
            self._rotate_right(z)
        elif y == z.right and x == y.right:
            self._rotate_left(z)
        elif y == z.right and x == y.left:
            self._rotate_right(y)
            self._rotate_left(z)
        else:
            raise Exception('_rebalance_node: z, y, x node configuration not recognized!')
    def _rotate_left(self, z):
        sub_root = z._parent
        y = z.right
        t2 = y.left
        y.left = z
        z._parent = y
        z.right = t2
        if t2 != None: t2._parent = z
        y._parent = sub_root
        if y._parent is None:
            self.root = y
        else:
            if y._parent.left == z:
                y._parent.left = y
            else:
                y._parent.right = y
        z.height = 1 + max(self.get_height(z.left),
            self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
            self.get_height(y.right))
    def _rotate_right(self, y):
        sub_root= y._parent
        z= y.left
        t3= z.right
        z.right= y
        y._parent = z
        y.left= t3
        if t3 is not None: t3._parent = y
        z._parent= sub_root
        if z._parent is None: 
            self.root = z
        else:
            if z._parent.left == y:
                z._parent.left = z
            else:
                z._parent.right = z
        y.height = 1 + max(self.get_height(y.left),
            self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left),
            self.get_height(z.right))
    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height
    
    def delete(self,book_id):
        if self.root is None:
            print("El árbol está vacío.")
            return
        node, parent=self._find_node_and_parent(book_id, self.root)
        if node is None:
            print("El libro no fue encontrado.")
            return
        # Caso 1: Nodo es una hoja
        if node.left is None and node.right is None:
            if parent is None:
                self.root= None
            elif parent.left == node:
                parent.left= None
            else:
                parent.right = None
            self._inspect_deletion(parent)
            return
        # Caso 2: Nodo tiene un hijo
        if node.left is None or node.right is None:
            child = node.left if node.left else node.right
            if parent is None:
                self.root= child
            elif parent.left == node:
                parent.left= child
            else:
                parent.right = child
            if child:  # Verificar si child existe antes de establecer el padre
                child._parent= parent
            self._inspect_deletion(parent)
            return
        # Caso 3: Nodo tiene dos hijos
        successor = self._find_minimum(node.right)
        node.book_id = successor.book_id
        self.delete(successor.book_id)


    def _find_node_and_parent(self, book_id,current_node,parent=None):
        if current_node is None:
            return None, None
        if book_id<current_node.book_id:
            return self._find_node_and_parent(book_id,current_node.left, current_node)
        elif book_id>current_node.book_id:
            return self._find_node_and_parent(book_id,current_node.right,current_node)
        else:
            return current_node, parent

    def _find_minimum(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current

    def _inspect_deletion(self,cur_node,path=[]):
        if cur_node is None:
            return
        path = [cur_node] + path
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height - right_height) > 1:
            if len(path) >= 3:
                self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + max(left_height, right_height)
        if new_height < cur_node.height:
            cur_node.height = new_height

        self._inspect_deletion(cur_node._parent, path)

        
    def get_root(self):
        return self.root.book_id, self.root.title, self.root.author

    def search_by_id(self, book_id):
        return self._search_by_id(self.root, book_id)

    def _search_by_id(self, node, book_id):
        if not node or node.book_id == book_id:
            return node

        if book_id<node.book_id:
            return self._search_by_id(node.left,book_id)
        
        return self._search_by_id(node.right,book_id)

    def search_by_title(self,title):
        result= []
        self._search_by_title(self.root, title, result)
        return result

    def _search_by_title(self, node, title, result):
        if node:
            self._search_by_title(node.left, title, result)
            if title.lower() in node.title.lower():
                result.append((node.book_id, node.title, node.author))
            self._search_by_title(node.right, title, result)

    def search_by_author(self, author):
        result =[]
        self._search_by_author(self.root, author, result)
        return result

    def _search_by_author(self,node,author,result):
        if node:
            self._search_by_author(node.left, author, result)
            if author.lower() in node.author.lower():
                result.append((node.book_id, node.title, node.author))
            self._search_by_author(node.right, author, result)

    def borrow_book(self, book_id):
        node = self._search_by_id(self.root, book_id)
        if node:
            if not node.borrowed:
                node.borrowed= True
                return True
            else:
                return False
        else:
            return None  # Book not found

    def return_book(self, book_id):
        node = self._search_by_id(self.root, book_id)
        if node:
            if node.borrowed:
                node.borrowed = False
                return True
            else:
                return False
        else:
            return None  # no se econtro el libro

    def _inorder_traversal(self, start, traversal):
        """Inorder traversal of our tree."""
        if start:
            traversal = self._inorder_traversal(start.left, traversal)
            traversal += (str(start.book_id) + '-' + start.title + '-' + start.author + '-' + ("Prestado" if start.borrowed else "Disponible") + '\n')
            traversal = self._inorder_traversal(start.right, traversal)
        return traversal

    def _preorder_traversal(self, start, traversal):
        """Preorder traversal of our tree."""
        if start:
            traversal += (str(start.book_id) + '-' + start.title + '-' + start.author + '-' + ("Prestado" if start.borrowed else "Disponible") + '\n')
            traversal = self._preorder_traversal(start.left, traversal)
            traversal = self._preorder_traversal(start.right, traversal)
        return traversal

    def _postorder_traversal(self, start, traversal):
        """Postorder traversal of our tree."""
        if start:
            traversal = self._postorder_traversal(start.left, traversal)
            traversal = self._postorder_traversal(start.right, traversal)
            traversal += (str(start.book_id) + '-' + start.title + '-' + start.author + '-' + ("Prestado" if start.borrowed else "Disponible") + '\n')
        return traversal
if __name__ == "__main__":
    # Menu of options
    def menu():
        avl = AVLTree()
        try:
            with  open ('Libros.json', "r") as file:
                data= json.load(file)
                for i in data['libros']:
                    avl.insert(i['id'],i['titulo'],i['autor'])
                print("i")
                file.close()
        except FileNotFoundError:
                print("File not found.")
        while True:
            print("\nAVL Book Tree\n"
                  + "\n\t1. Esta el arbol vacio"
                  + "\n\t2. Agregar libro"
                  + "\n\t3. Borrar libro"
                  + "\n\t4. Recorrer Inorder"
                  + "\n\t5. Recorrer Preorder"
                  + "\n\t6. Recorrer Postorder"
                  + "\n\t7. Buscar libro por Id"
                  + "\n\t8. Buscar libro por titulo"
                  + "\n\t9. Buscar libro por autor"
                  + "\n\t10. prestar"
                  + "\n\t11. devolver"
                  + "\n\t12. Obtener la raiz"
                  + "\n\t13. Salir")
            
            opc = int(input("\nEscoja una opcion: "))
            if opc == 1:
                if avl.root is None:
                    print("El arbol esta vacio?")
                else:
                    print("El arbol no esta vacio")
            elif opc == 2:
                book_id = int(input("\nIngrese el id del libro: "))
                author = input("Ingrese el autor: ")
                title = input("ingrese el titulo: ")
                avl.insert(book_id, title, author)
            elif opc == 3:
                book_id = int(input("\nIngrese el id del libro: "))
                avl.delete(book_id)
                print("libro con el ID", book_id, "borrado")
            elif opc == 4:
                print("Inorder: \n", avl._inorder_traversal(avl.root, ""))
            elif opc == 5:
                print("Preorder: \n", avl._preorder_traversal(avl.root, ""))
            elif opc == 6:
                print("Postorder: \n", avl._postorder_traversal(avl.root, ""))
            elif opc == 7:
                book_id = int(input("\nIngrese el id que quiere buscar: "))
                result = avl.search_by_id(book_id)
                if result:
                    print(f"Se encontro- ID: {result.book_id}, Titulo: {result.title}, Autor: {result.author}, Estado: {'Prestado' if result.borrowed else 'disponible'}")
                else:
                    print("Libro no encontrado")
            elif opc == 8:
                title = input("\nIngrese el titulo del libro: ")
                result = avl.search_by_title(title)
                if result:
                    print("Libro encontrado:")
                    for book in result:
                        print(f"ID: {book[0]}, Titulo: {book[1]}, Autor: {book[2]}")
                else:
                    print("No tenemos ese libro.")
            elif opc == 9:
                author = input("\nIngrese el autor del libro: ")
                result = avl.search_by_author(author)
                if result:
                    print("libro encontrado:")
                    for book in result:
                        print(f"ID: {book[0]}, Titulo: {book[1]}, Autor: {book[2]}")
                else:
                    print("No tenemos libros de ese autor.")
            elif opc == 10:
                book_id = int(input("Ingrese el id del libro: "))
                result = avl.borrow_book(book_id)
                if result == True:
                    print("El libro fue prestado con exito.")
                elif result == False:
                    print("El libro no esta disponible para prestamos")
                else:
                    print("no se encontro el libro")
            elif opc ==11:
                book_id = int(input("Ingrese el id del libro que desea devolver:"))
                result = avl.return_book(book_id)
                if result == True:
                    print("Fue entregado con exito")
                elif result == False:
                    print("El libro ya estaba disponible")
                else:
                    print("No se encontro el libro")
            elif opc == 12:
                root = avl.get_root()
                if root:
                    print(f"Root: ID: {root[0]}, Titulo: {root[1]}, Autor: {root[2]}")
                else:
                    print("El arbol esta vacio")
            elif opc == 13:
                break
            else:
                print("Error ingrese una opcion entre el 1-11")

    menu()
