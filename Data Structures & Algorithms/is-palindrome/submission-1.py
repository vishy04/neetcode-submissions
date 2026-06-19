class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lower_str = "".join(s.lower())
        n = len(lower_str)
        i, j= 0, n - 1

        while i < j:
            while i < j and not self.isalphanum(lower_str[i]):
                #skipping if not alphanum
                i += 1
            while i < j and not self.isalphanum(lower_str[j]):
                j -= 1 
            if lower_str[i] != lower_str[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    def isalphanum( self, c:str )->bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9')
                    )
