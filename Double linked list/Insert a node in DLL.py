#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_position(position,data,head):
    new_node = node(data)
    if head is None:
        return new_node
    temp = head
    count = 0

    while temp.next is not None and count < position:
        temp = temp.next
        count +=1
    new_node.next = temp.next
    new_node.prev = temp
    if temp.next:
        temp.next.prev = new_node
    temp.next = new_node
    return head
