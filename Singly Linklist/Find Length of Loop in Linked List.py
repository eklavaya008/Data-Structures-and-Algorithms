#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def FindLengthLL(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                count+=1
                slow = slow.next
            return count
    return 0
