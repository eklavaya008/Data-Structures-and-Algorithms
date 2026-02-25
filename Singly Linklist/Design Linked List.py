#Solution

class Node:
    def __init__(self, val=0, next=None):
        self.val = val              
        self.next = next            

class MyLinkedList:
    def __init__(self):
        self.head = None            
        self.size = 0              

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):      
            temp = temp.next
        return temp.val

    def addAtHead(self, val):
        node = Node(val, self.head) 
        self.head = node            
        self.size += 1

    def addAtTail(self, val):
        node = Node(val)
        if not self.head:         
            self.head = node
        else:
            temp = self.head
            while temp.next:        
                temp = temp.next
            temp.next = node        
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        if index > self.size:       
            return
        if index == 0:              
            self.addAtHead(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next    
            node = Node(val, prev.next)
            prev.next = node       
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:  
            return
        if index == 0:                       
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next            
            prev.next = prev.next.next     
        self.size -= 1