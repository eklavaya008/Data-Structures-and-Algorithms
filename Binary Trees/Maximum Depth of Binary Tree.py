class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        left_height =self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height,right_height) 
    
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(8)
root.right.left.left.right = TreeNode(9)
root.right.right = TreeNode(7)


sol = Solution()
print(sol.maxDepth(root))

