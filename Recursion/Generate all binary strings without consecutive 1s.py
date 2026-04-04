#Solution

class Solution:
    def solve(self,index,flag,nums,result):
        if index >= len(nums):
            result.append("".join(nums))
            return
        nums[index] = "0"
        self.solve(index+1,True,nums,result)
        if flag == True:
            nums[index] = "1"
            self.solve(index+1,False,nums,result)
            nums[index] = "0"
    def generatebinaryString(self,n):
        nums = ["0"]*n
        result = []
        self.solve(0,True,nums,result)
        return result
    
sol = Solution()
nums = 3
print(sol.generatebinaryString(nums))

