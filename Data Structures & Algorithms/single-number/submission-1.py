class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] =  count.get(num,0) + 1
        
        for val in count:
            if count[val] == 1:
                return val
                