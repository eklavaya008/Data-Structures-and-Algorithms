class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def createTree(self, root, l):

        root.left = Node(l[1])
        root.right = Node(l[2])

        root.left.left = Node(l[3])
        root.left.right = Node(l[4])

        root.right.left = Node(l[5])
        root.right.right = Node(l[6])

l = [1,2,3,4,5,6,7]
root = Node(l[0])
sol = Solution()
sol.createTree(root,l)
print(root.data)              
print(root.left.data)        
print(root.right.data)        
print(root.left.left.data)    
print(root.left.right.data)  
print(root.right.left.data)  
print(root.right.right.data)  


