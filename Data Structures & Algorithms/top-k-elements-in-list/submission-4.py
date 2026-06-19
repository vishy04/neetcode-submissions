from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashing 
        # nums = [1,2,2,3,3,3,2,0], k = 2

        freq = defaultdict(int) #extra space
        for num in nums:
            freq[num] += 1
        # {0:1, 1:1 , 2:3, 3:3}

        return sorted(freq.keys(), 
                    key = lambda x:freq[x], 
                    reverse = True)[:k]
        

