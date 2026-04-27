#Solution

class Solution:
    def postToPre(self, post_exp):
        stack = []
        for char in post_exp:
            if char.isalnum():
                stack.append(char)
            
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                new_operand = f"{char}{operand1}{operand2}"
                stack.append(new_operand)
        return stack[-1]

        