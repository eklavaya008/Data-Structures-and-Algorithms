#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def reverse(self, head):
    if head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.next = prev
        curr.prev = front
        prev = curr
        curr = front
    return prev
    
