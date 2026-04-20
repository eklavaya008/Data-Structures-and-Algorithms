#Solution

class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class myQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        

    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
  
    def dequeue(self):
        if self.front == None:
            return -1
        if self.front == None:
            self.rear = None
        popped = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return popped
        

    def getFront(self):
        if self.front == None:
            return -1
        return self.front.data
        

    def size(self):
        current = self.front
        count =  0
        while current:
            count += 1
            current = current.next
        return count
    
