class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = longest = 0 
        freq_count = [0] * 26
        for right in range(n):
            curr_index = ord(s[right]) - ord('A')
            """
            window_length - max(freq_count) < k 
            this means that the char we have - the max time a char is repeated
            this give the number of changes we need to do in order to 
            achieve a valid state
            Simply this tell me the char I need to change , to make it a valid substring
            """
            #VALID_STATE
            freq_count[curr_index] += 1

            # INVALID_STATE
            while (right - left + 1) - max(freq_count) > k :
                #decrease the count of the char on left
                freq_count[ord(s[left]) - ord('A')] -= 1
                # move left ahead 
                left += 1

            

            longest = max(longest, right - left + 1)
        
        return longest


            
            