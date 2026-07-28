#Solution

class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        window = 0
        left  = 0
        ans = float('inf')

        for right in range(n):
            window += nums[right]
            while window >= target:
                ans = min(ans, right - left + 1)
                window -= nums[left]
                left += 1
                
        return 0 if ans == float('inf') else ans
