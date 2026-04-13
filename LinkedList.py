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

    def reverseList(head):
        prev = None
        while head is not None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
        return prev

    def sortList(head):
        if head is None:
            return head
        changed = True 
        
        while changed:
            changed = False
            current = head
            while current.next is not None:
                if current.value > current.next.value:
                    temp= current.value
                    current.valeue = current.next.value
                    current.next.value = temp
                    changed = True
                current = current.next
        return head

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
            
    def size(self):
        current = self.head
        listSize = 0
        while current is not None:
            listSize += 1
            current = current.next   
        return listSize    
    
