"""
The concept of a stack,
a last-in/first-out construct, is integral to the left-to-right evaluation of RPN. In the example 3 4 −,
first the 3 is put onto the stack, then the 4; the 4 is now on top and the 3 below it. The subtraction operator removes the top two items from the stack, performs 3 − 4, and puts the result of −1 onto the stack.
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        stack = []
        for token in tokens:
            if token not in valid_operators:
                stack.append(token)
            else:
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                # perform v1 token v2, but token is string( to solve this using lambda)
                result = valid_operators[token](v1, v2)
                stack.append(result)
        
        return int(stack[-1])
