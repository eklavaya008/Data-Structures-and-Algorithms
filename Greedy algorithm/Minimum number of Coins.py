#Solution

class Solution:
    def findMin(self, n):
        coins = [1,2,5,10]
        num = len(coins)
        count = 0 
        for i in range(num-1,-1,-1):
           while n>=coins[i]:
               count+=1
               n-=coins[i]
        return count
    
sol = Solution()
n = 39
print(sol.findMin(n))

