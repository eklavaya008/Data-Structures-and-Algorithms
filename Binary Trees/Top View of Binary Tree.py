class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def topView(self, root):
        if root is None:
            return 0
        ans = []
        queue = deque()
        result = {}
        queue.append((root,0))
        while queue:
            e , line = queue.popleft()
            if line not in result:
                result[line] = e.data
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans
    
