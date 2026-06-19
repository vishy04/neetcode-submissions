class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = longest = 0 
        freq_count = [0] * 26
        
        for right in range(n):
            # 1. WINDOW EXPANSION: Add current character to frequency map
            curr_index = ord(s[right]) - ord('A')
            freq_count[curr_index] += 1
            
            # 2. VALIDITY CHECK:
            # Logic: (Total Window Length) - (Frequency of Most Frequent Char) = Changes Needed
            # If "Changes Needed" > k, the window is in an INVALID_STATE.
            """
            Mathematical Logic:
            (right - left + 1) - max(freq_count) > k 
            
            - (right - left + 1): This is our current window size.
            - max(freq_count): The most frequent character we are trying to match everything else to.
            - The difference represents the number of 'other' characters we must replace.
            - If this difference exceeds 'k', we must shrink the window from the left.
            """
            while (right - left + 1) - max(freq_count) > k:
                # Decrease frequency of character at 'left' and shrink window
                freq_count[ord(s[left]) - ord('A')] -= 1
                left += 1

            # 3. RESULT UPDATE: Record the maximum length of any VALID_STATE encountered
            longest = max(longest, right - left + 1)
        
        return longest