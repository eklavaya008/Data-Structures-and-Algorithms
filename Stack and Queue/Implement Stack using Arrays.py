#Solution

class myStack:
    def __init__(self, n):
        self.items = []
        self.capacity = n

    
    def isEmpty(self):
        return len(self.items) == 0

    
    def isFull(self):
        return len(self.items) == self.capacity

    
    def push(self, x):
        if len(self.items) == self.capacity:
            return False
        self.items.append(x)
        return True

    
    def pop(self):
        if len(self.items) == 0:
            return -1
        return self.items.pop()
        

    
    def peek(self):
        if not self.items:
            return -1
        return self.items[-1]
    