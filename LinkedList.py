from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    #Insertar al inicio
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Insertar al final
    def insert_at_end(self, data):
        nuevo = Node(data)

        if self.head is None:
            self.head = nuevo
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = nuevo

    # Mostrar Lista 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Buscar elemento
    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True
            current = current.next

        return False
    
    #Eliminar primer elemento
    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

