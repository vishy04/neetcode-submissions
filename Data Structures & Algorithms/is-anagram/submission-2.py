class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return false if length is not equal 

        if len(s) != len(t):
            return False 

        #we will keep a track of the character in s , t [in one list]
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 #+1 in s 
            count[ord(t[i]) - ord('a')] -= 1 #-1 in t 

        '''if they are anagram the count will have all entry zero , 
        as the character present in s lead to +1 ,
        but the same character position in t will be -1 , resulting in 
        all zero count again '''

        for val in count :
            if val!= 0:
                return False

        return True 

        











