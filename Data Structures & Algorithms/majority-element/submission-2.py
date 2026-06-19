class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1 :
            return nums[0]

        for num in nums:
            """
            Go through the list. Every time you see num, 
            generate a 1. Then, sum all those 1s together.
            """
            count = sum(1 for i in nums if i == num)
    
            if count > n // 2:
                return num
                  
