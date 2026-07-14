#Solution

class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[i],nums[k] = nums[k],nums[i]
                k +=1
        return k
