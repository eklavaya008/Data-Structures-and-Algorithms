#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def middleNode(head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

