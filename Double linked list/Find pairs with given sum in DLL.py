#Solution

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def find_pairDLL(head,target):
    left = head
    right = head
    result = []
    while right.next:
        right = right.next
    while left is not None and right is not None and left.data<right.data:
        total = left.data + right.data
        if total == target:
            result.append([left.data,right.data])
            left = left.next
            right = right.prev
        elif total >target:
            right = right.prev
        else:
            left = left.next
    return result