class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def solve(self,root):
        if not root:
            return 0
        l_sum = self.solve(root.left)
        r_sum = self.solve(root.right)
        if l_sum < 0:
            l_sum = 0
        if r_sum < 0:
            r_sum = 0
        self.maxi = max(self.maxi,l_sum+root.val+r_sum)
        return root.val + max(l_sum , r_sum)
    def maxPathSum(self, root):
        self.maxi = float("-inf")
        self.solve(root)
        return self.maxi