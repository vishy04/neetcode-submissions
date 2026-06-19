
class Solution:

    def curr_index(self,s: str, idx:int):
        return ord(s[idx]) - ord('A')

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        left = max_length = 0 
        #keeping the count of char currently in the window
        freq_count = [0] * 26 

        for right in range(n):
            #Valid State
            freq_count[self.curr_index(s,right)] += 1

            # Invalid State
            """
            No. of element needed to change -> (right - left) - max(freq_count)
            """
            while (right - left + 1) - max(freq_count) > k:
                freq_count[self.curr_index(s,left)] -= 1
                left += 1
            
            max_length = max(right - left + 1, max_length)
        
        return max_length




