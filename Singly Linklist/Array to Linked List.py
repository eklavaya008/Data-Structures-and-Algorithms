#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def arrayToList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head
