class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def solve(self,root,level,ans):
        if not root:
            return []
        if len(ans) == level:
            ans.append(root.val)
        if root.right:
            self.solve(root.right,level+1,ans)
        if root.left:
            self.solve(root.left,level+1,ans)
    def rightSideView(self, root):
        ans = []
        self.solve(root,0,ans)
        return ans
    
