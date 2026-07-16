#Solution

class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        seen = set()
        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False
