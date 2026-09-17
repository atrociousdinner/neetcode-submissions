class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if ord(token) >= ord('0') and ord(token) <= ord('9'):
                stack.append(token)
            else:
                 first_operand = int(stack.pop())
                 operator = token
                 result = eval(f"{first_operand} {operator} {int(stack.pop())}")
                 stack.append(result)
        return stack[-1]        