class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        return (
            [root.val] +
            self.preorderTraversal(root.left) +
            self.preorderTraversal(root.right)
        )
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.preorderTraversal(root))
