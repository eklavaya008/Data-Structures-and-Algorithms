class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findCeil(self,root, x):
        temp = root
        ciel = -1
        while temp is not None:
            if temp.data == x:
                return temp.data
            elif temp.data < x:
                temp = temp.right
            else:
                ciel = temp.data
                temp = temp.left
        return ciel

