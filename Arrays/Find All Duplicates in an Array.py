class Solution(object):
    def findDuplicates(self, nums):
        freq = {}
        ans = []

        for num in nums:
            freq[num] = freq.get(num,0)+1

        for num in freq:
            if freq[num] > 1:
                ans.append(num)
        
        return ans
