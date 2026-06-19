class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #without using set - using hashmap for storing current element and there index
        n = len(s)
        left = 0 #starting pointer
        char_dict = {} #to track substring elements(unique)
        max_length = 0

        for right in range(n):
            """
            invalid state - when curr_element is present in char_dict,
            then remove from char_dict and move left pointer
            """
            if s[right] in char_dict:
                left = max(char_dict[s[right]] + 1, left)
            # Valid State: Add new character and update the max_length
            char_dict[s[right]] = right
            #calulating the length of substring
            length = (right - left) + 1

            max_length = max(length, max_length)

        return max_length


