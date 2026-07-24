#Solution 

class Solution(object):
    def findMaxAverage(self, nums, k):
        window = 0

        for i in range(k):
            window += nums[i]

        ans = window

        for i in range(k,len(nums)):
            window += nums[i] 
            window -= nums[i-k] 
            ans = max(ans,window)

        return ans/float(k)