class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Revision ( 23 Jul )
        if len(s) != len(t):
            return False
        hash = {}
        for char in s:
            hash[char] = hash.get(char,0) + 1
        
        for char in t:
            if hash.get(char):
                hash[char] -= 1
            else:
                return False
        return True if hash.values() else False