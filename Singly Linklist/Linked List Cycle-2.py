#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def LinkedLCycle2(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None