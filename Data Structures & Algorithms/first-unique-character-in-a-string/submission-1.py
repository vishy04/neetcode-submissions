class Solution:
    def firstUniqChar(self, s: str) -> int:
        #as string has only lowercase_english_letter
        hash_list = [0] * 26

        for char in s:
            asci = ord(char)-ord("a")
            hash_list[asci] += 1
        
        for i in range(len(s)):
            asci = ord(s[i])-ord("a")
            if hash_list[asci] == 1:
                return i
        return -1
                