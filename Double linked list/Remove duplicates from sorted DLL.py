#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def remove_dupliDLL(head):
    curr = head
    while curr:
        if curr.prev and curr.prev.data == curr.data:
            if curr.prev == head:
                curr.prev = None
                head = curr 
            else:
                curr.prev.prev.next = curr
                curr.prev = curr.prev.prev
        curr = curr.next
    return head
