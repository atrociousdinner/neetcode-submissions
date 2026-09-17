class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    if b == 0:
                        raise ZeroDivisionError("Cannot divide by zero in RPN expression")
                    stack.append(int(a/b))
            else:
                stack.append(int(token))

        return stack[0]
