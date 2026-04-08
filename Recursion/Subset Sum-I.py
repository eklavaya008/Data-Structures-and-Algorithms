#Solution

class Solution:
    def solve(self,index,total,arr,result):
        if index>= len(arr):
            result.append(total)
            return
        sums = total + arr[index]
        self.solve(index+1,sums,arr,result)
        sums = total
        self.solve(index+1,sums,arr,result)
    def subsetSums(self, arr):
        result = []
        self.solve(0,0,arr,result)
        return result
    
sol = Solution()
arr = [5,9,3]
print(sol.subsetSums(arr))
