class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower_str = "".join(char.lower() for char in s if char.isalnum())
        n = len(lower_str)
        i, j= 0, n - 1

        while i < j:
            if lower_str[i] != lower_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
