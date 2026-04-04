#Solution

class Solution:
    def solve(self,index,nums,result):
        if index >=len(nums):
            result.append("".join(nums))
            return
        nums[index] = "0"
        self.solve(index+1,nums,result)
        nums[index] = "1"
        self.solve(index+1,nums,result)
    
    def binstr(self, n):
        nums = ["0"]*n
        result = []
        self.solve(0,nums,result)
        return result
    
sol = Solution()
nums = 3
print(sol.binstr(nums))
