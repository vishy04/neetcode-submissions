class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {} #char -> freq
        for char in s:
            hash[char] = hash.get(char,0) + 1
        
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        
        return -1