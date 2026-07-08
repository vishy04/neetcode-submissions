class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        
        # Battle Scar 3 & 4: Use a dictionary, and seed it for index 0
        sum_cache = {0: 1}  

        for i in range(len(nums)):
            running_sum += nums[i]
            
            # Battle Scar 1: The correct math equation
            complement = running_sum - k  
            
            # Battle Scar 2: Check history BEFORE updating it
            if complement in sum_cache:
                count += sum_cache[complement] 
                
            sum_cache[running_sum] = sum_cache.get(running_sum, 0) + 1
            
        return count