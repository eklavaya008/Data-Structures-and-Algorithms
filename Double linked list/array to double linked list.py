#Solution

class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None
        self.prev = None



def constructDLL(self, arr):
    if not arr:
        return None
            
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        prev.next = new_node
        new_node.prev = prev
        prev = new_node
    return head
