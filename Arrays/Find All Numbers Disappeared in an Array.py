class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = set()
        ans = []

        for num in nums:
            seen.add(num)
        
        for i in range(len(nums)):
            if i+1 in seen:
                continue
            else:
                ans.append(i+1)
        return ans
        
