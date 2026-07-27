#Solution

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        window = 0
        freq = {}

        for i in range(k):
            freq[nums[i]] = freq.get(nums[i],0) + 1
            window += nums[i]

        ans = window if len(freq) == k else 0

        for i in range(k,len(nums)):
            outgoing = nums[i-k]
            window -= outgoing
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            incoming = nums[i]
            window += incoming
            freq[incoming] = freq.get(incoming,0) + 1


            if len(freq) == k:
                ans = max(ans,window)

        return ans

