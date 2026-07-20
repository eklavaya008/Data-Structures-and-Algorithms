#Solution

class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        maxi = 0
        for i in range(n):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth+=accounts[i][j]
            maxi = max(maxi,wealth)
        return maxi
