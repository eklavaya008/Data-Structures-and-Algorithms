#Solution

class myQueue:
    def __init__(self, n):
        self.items = []
        self.capacity = n
    
    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        if len(self.items) == self.capacity:
            return True
        return False
        
    def enqueue(self, x):
        if len(self.items) == self.capacity:
            return False
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            return -1
        self.items.pop(0)

    def getFront(self):
        if not self.items:
            return -1
        return self.items[0]
       
    def getRear(self):
        if not self.items:
            return -1
        return self.items[-1] 
    
