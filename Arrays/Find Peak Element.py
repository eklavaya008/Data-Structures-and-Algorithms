#Solution

class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)

        if n == 1 or nums[0] >nums[1]:
            return 0
        
        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        return n-1
