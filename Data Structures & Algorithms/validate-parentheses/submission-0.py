class Solution:
    def isValid(self, s: str) -> bool:

        mapped = {")": "(", "}": "{", "]": "["}
        stack = []

        # add if closing bracket
        for char in s:
            if char in mapped:
                if stack and stack[-1] == mapped[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack :return True
        else: return False

        # remove if opening bracked ( if empty false )
        # final state of stack should be empty for it be true
