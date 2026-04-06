#Solution

class Solution(object):
    def backtrack(self,index,total, bracket,result):
        if index>=len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return
        if total>len(bracket)//2:
            return
        elif total < 0:
            return
        bracket[index] = "("
        sum = total +1
        self.backtrack(index+1,sum,bracket,result)
        bracket[index] = ")"
        sum = total -1
        self.backtrack(index+1,sum,bracket,result)

    def generateParenthesis(self, n):
        bracket = [""]*(n*2)
        result = []
        self.backtrack(0,0,bracket,result)
        return result


sol = Solution()
n =3
print(sol.generateParenthesis(n))
