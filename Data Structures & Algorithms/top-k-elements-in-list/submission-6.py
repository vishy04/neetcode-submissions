from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #bucket sort 
        count = defaultdict(int)
        #key is count and val is values appearing key times[list]
        hash_list = [[] for i in range(len(nums)+1)] 

        # creating count dict
        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            hash_list[freq].append(num)
        
        result = []

        for i in range(len(hash_list)-1 , 0, -1):
            for num in hash_list[i]:
                result.append(num)
                if len(result) == k:
                    return result


