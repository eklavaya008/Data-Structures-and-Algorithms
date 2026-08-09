#Solution

class Solution(object):
    def triangleNumber(self, nums):
        n = len(nums)
        nums.sort()
        count = 0

        for k in range(n):

            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count +=  j - i
                    j -= 1
                else:
                    i += 1
        return count

