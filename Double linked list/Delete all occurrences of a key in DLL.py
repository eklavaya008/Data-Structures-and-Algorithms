#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def deleteAllOccurOfX(head, x):        
        while head and head.data == x:
            head = head.next
            if head:
                head.prev = None        
        temp = head          
        while temp:
            if temp.data == x:
                prev_node = temp.prev
                next_node = temp.next
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
            temp = temp.next
        return head
