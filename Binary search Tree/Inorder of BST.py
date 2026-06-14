class Solution:
    def isBSTTraversal(self, arr):
        n = len(arr)
        
        for i in range(1,n):
            if arr[i] <= arr[i-1]:
                return False
        return True
