#Solution

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in freq:
                if abs(freq[nums[i]] - i) <= k:
                    return True
            freq[nums[i]] = i
        return False
