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
            
    # Método para reversar la lista
    def reverseList(head):
        prev = None
        current = head
        while current is not None:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
        return prev
    
    # Ordena una lista enlazada simple en orden ascendente reorganizado los punteros y sus nodos
    def sortList(head):
        if head is None or head.next is None:
            return head
        sorted_Head = None 
        current = head

        while current is not None:
            next_node = current.next
            if sorted_Head is None or current.value < sorted_Head.value:
                current.next = sorted_Head
                sorted_Head = current 
            else:
                temp = sorted_Head
                while temp.next is not None and temp.next.value < current.value:
                    temp= temp.next
                current.next = temp.next
                temp.next= current
            current = next_node
        return sorted_Head

    #Metodo para eliminar por valor
    def deleteByValue(self, value):
        if self.head is None:
            print("Lista vacia")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            print(value + " elimnado de la lista")
            return
        current = self.head
        
        while current is not None:
            if current.next.data == value:
                current.head = current.next.next
                print(value + " elimnado de la lista")
                return
            current = current.next
        print("Valor no esta en la lista")
            
    #Metodo para determinar el tamaño de la lista enlazada        
    def size(self):
        current = self.head
        listSize = 0
        while current is not None:
            listSize += 1
            current = current.next   
        return listSize    
    
