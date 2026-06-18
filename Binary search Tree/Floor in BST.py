class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMaxFork(self, root, k):
        temp = root
        floor = -1
        while temp:
            if temp.data == k:
                return temp.data
            elif temp.data > k:
                temp = temp.left
            else:
                floor = temp.data
                temp = temp.right
        return floor

