#Solution

class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        result = []
        bag = 0
        for i in range(n):
            bag+=nums[i]
            result.append(bag)
        return result
