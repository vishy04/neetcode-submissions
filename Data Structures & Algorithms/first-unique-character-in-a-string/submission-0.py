class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_dict = {} # value:freq

        for char in s:
            hash_dict[char] = hash_dict.get(char, 0) + 1
        
        for i  in range(len(s)):
            if hash_dict[s[i]] == 1:
                return i 

        return -1            
