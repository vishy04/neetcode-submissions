class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        left = 0 #starting pointer
        ele_set = set() #to track substring elements(unique)
        max_length = 0

        for right in range(n):
            #when curr_element is present in ele_set,
            #then remove from ele_set and move left pointer

            while s[right] in ele_set:
                ele_set.remove(s[left])
                left += 1
            
            ele_set.add(s[right])
            #calulating the length of substring
            length = (right - left) + 1
            
            max_length = max(length, max_length)

        return max_length


