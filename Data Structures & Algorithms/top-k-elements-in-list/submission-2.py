from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashing 
        # nums = [1,2,2,3,3,3,2,0], k = 2

        freq = defaultdict(int) #extra space
        for num in nums:
            freq[num] += 1
        # {0:1, 1:1 , 2:3, 3:3}

        #temp_final = [[freq, num]]
        temp = [] #extra space
        for key, val in freq.items():
            temp.append([val, key])

        temp.sort()

        result = [] #extra space

        #Store till the result list is == k ;
        while len(result) < k:
            #storing first k from temp_sorted list
            result.append(temp.pop()[1])
        
        return result

