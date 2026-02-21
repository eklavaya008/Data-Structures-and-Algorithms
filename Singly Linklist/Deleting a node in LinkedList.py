#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteNode(node):
        node.data = node.next.data
        node.next = node.next.next