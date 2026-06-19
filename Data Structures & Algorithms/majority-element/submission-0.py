from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #hashing solution 

        freq = defaultdict(int)
        res = max_count = 0
        for num in nums:
            freq[num] += 1
            if max_count < freq[num]:
                max_count = freq[num] 
                res = num
        
        return res
                
            
