#Solution

class Solution:
    def preToPost(self, pre_exp):
        stack = []
        for char in pre_exp[::-1]:
            if char.isalnum():
                stack.append(char)
            
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_operand = f"{operand1}{operand2}{char}"
                stack.append(new_operand)
        return stack[-1]
    
