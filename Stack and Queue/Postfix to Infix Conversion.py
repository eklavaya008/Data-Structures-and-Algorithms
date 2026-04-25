#Solution

class Solution:
    def postToInfix(self, postfix):
        stack = []
        for char in postfix:
            if char.isalnum():
                stack.append(char)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                new_operand = f"({operand1}{char}{operand2})"
                stack.append(new_operand)
        return stack[-1]
