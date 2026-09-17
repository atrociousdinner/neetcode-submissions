class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not(ord(token) >= ord('0') and ord(token) <= ord('9')):
                first_operand = int(stack.pop())
                operator = token
                result = eval(f"{first_operand} {operator} {int(stack.pop())}")
                stack.append(result)
            else:
                stack.append(token)
                
        return stack[-1]        