class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        temp = root

        while temp:
            if temp.val < val:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
            elif temp.val > val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
        return root
    
