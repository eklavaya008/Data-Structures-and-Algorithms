#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def delete_node(head,pos):
    if pos == 1:
        head = head.next
        if head:
            head.prev = None
        return head
    temp = head
    count = 1
    while temp is not None and count < pos:
        temp = temp.next
        count += 1
    if temp is not None:
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
    return head
