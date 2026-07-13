class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #1. Calculate all subarrays iteratively (O(n^2)-> TC) / Runtime Error
        # for i -> end
            # for j: i+1 -> end
        """
        
        
        """
        

        # presum : frequency
        # Why {0:1} -> because we for subarray [i,j]n we need to subtract cache[j] - cache[i-1]
        #if i == 0 we can get in trouble with out of bond thats my we put 0 , has no effect in sub and add operations
        #Pre calculating the sum till every index
        cache = {0:1} 

        # array = [2   -1  1   2]
        count = 0
        running_sum = 0
        for idx , num in enumerate(nums):
            running_sum += num
            target = running_sum - k
            if target in cache:
                count += cache[target]
            cache[running_sum] = cache.get(running_sum, 0) + 1
        
        # cache = {0:1, 1:1, 2:2, 4:1}
        #Error -> We cannot do double check because we need to find left boundary iterating on right boundary
        # Means if we iterate through j , when we find index i , we need to have i < j
        """
        count = 0
        for num in nums:
            target = num - k
            if target in cache:
                count += cache[target]
        """

        return count