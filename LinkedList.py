
class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True
            current = current.next

        return False  

    def deleteByValue(self, value):
        if self.head is None:
            print("Lista vacia")
        
        if self.search(value) == True:
            self.head = self.head.next
        else:
            print("Value not in List")
            
    def size(self):
        current = self.head
        listSize = 0
        while current is not None:
            listSize += 1
            current = current.next   
        return listSize    
    