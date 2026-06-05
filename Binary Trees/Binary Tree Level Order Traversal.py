class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            level = []
            size = len(queue)
            for _ in range(size):
                e = queue.popleft()
                level.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            result.append(level)
        return result
    



