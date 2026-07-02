class Solution:
    def isValid(self, s: str) -> bool:

        # closed -> open mapping
        mapped = {")": "(", "}": "{", "]": "["}
        stack = []

        # add if closing bracket
        for char in s:
            if char in mapped:  # char is closing bracket
                # remove if opening bracked 
                #confusion in the fact that why is it necessary that top element has to match
                # try this eg "{[}]"
                if stack and stack[-1] == mapped[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack