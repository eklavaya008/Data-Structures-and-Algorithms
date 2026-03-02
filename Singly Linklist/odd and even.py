#Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def oddeven(head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head
