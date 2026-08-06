#Solution

class Solution(object):
    def sortColors(self, nums):
        i = 0
        j = len(nums) - 1
        current = 0

        while current <= j:
            if nums[current] == 0:
                nums[i],nums[current] = nums[current],nums[i]
                i+=1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current],nums[j] = nums[j],nums[current]
                j-=1
        
        return nums
