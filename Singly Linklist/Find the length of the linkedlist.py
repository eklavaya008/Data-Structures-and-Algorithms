#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def LenghtofSLL(head):
    count = 0
    temp = head

    while temp is not None:
        count+=1
        temp = temp.next
    return count