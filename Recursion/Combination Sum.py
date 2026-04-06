#Solution

class Solution(object):
    def backtrack(self,index,total,subset,nums,target,result):
        if total == target:
            result.append(subset[:])
            return
        elif total > target:
            return
        if index >= len(nums):
            return 
        sums = total + nums[index]
        subset.append(nums[index])
        self.backtrack(index,sums,subset,nums,target,result)
        sums = total
        subset.pop()
        self.backtrack(index+1,sums,subset,nums,target,result)
    def combinationSum(self, candidates, target):
        result = []
        self.backtrack(0,0,[],candidates,target,result)
        return result
    