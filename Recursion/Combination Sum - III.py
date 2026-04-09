#Solution

class Solution(object):
    def solve(self,n,last,total,subset,k,result):
        if total == n and len(subset) == k:
            result.append(subset[:])
            return
        if total>n or len(subset)> k:
            return

        for i in range(last,10):
            sums = total+i
            subset.append(i)
            self.solve(n,i+1,sums,subset,k,result)
            subset.pop()
    def combinationSum3(self, k, n):
        result = []
        self.solve(n,1,0,[],k,result)
        return result
        
sol = Solution()
print(sol.combinationSum3(3,7))
