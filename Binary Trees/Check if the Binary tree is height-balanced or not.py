class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def solve(self,root):
        if root is None:
            return 0
        left_height = self.solve(root.left)
        if left_height == -1:
            return -1
        right_height = self.solve(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height , right_height)

    def isBalanced(self, root):
        height = self.solve(root)
        if height == -1:
            return False
        return True 
    
