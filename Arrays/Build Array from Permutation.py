#Solution

class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans
