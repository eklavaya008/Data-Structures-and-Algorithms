#Solution

class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        result = 0
        non_1 = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                non_1 += 1
            
            while non_1 > 1:
                if nums[left] != 1:
                    non_1 -= 1
                left += 1
            
            result = max(result, right-left)
        
        return result

