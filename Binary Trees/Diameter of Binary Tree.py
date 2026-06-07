class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    diameter = 0
    def calculateHeight(self,root):
        if not root:
            return 0
        left_height = self.calculateHeight(root.left)
        right_height = self.calculateHeight(root.right)
        self.diameter = max(self.diameter,left_height + right_height)
        return 1 + max(left_height,right_height)


    def diameterOfBinaryTree(self, root):
        self.calculateHeight(root)
        return self.diameter
    
