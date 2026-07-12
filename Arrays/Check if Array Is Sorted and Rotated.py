#Solution

class Solution(object):
    def check(self, nums):
        n = len(nums)
        drop = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drop +=1
        if drop > 1:
            return False
        else:
            return True
