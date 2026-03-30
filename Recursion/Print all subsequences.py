#Solution

class Solution(object):
    def func(self,index, subset, nums, result):
        if index >= len(nums):
            result.append(subset[:])
            return 
        subset.append(nums[index])
        self.func(index+1, subset, nums, result)
        subset.pop()
        self.func(index+1, subset, nums , result)

    def subsets(self, nums):
        result = []
        self.func(0,[],nums,result)
        return result

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))