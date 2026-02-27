#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def ReverseLL(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev
