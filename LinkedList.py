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

class LinkedList:
    def __init__(self):
        self.head = None  

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
    
