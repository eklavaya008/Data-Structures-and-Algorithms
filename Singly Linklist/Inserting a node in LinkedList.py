Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insertNode(head,x):
    new_Node = Node(x)
    if head is None:
        return new_Node
    current = new_Node
    while current is not None:
        current = current.next
    current.next = new_Node
    return head