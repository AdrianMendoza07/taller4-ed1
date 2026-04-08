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