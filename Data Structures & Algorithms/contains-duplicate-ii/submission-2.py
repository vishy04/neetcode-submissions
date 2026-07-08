class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        INTUITION:
        Track the last seen index of each number using a hash map. 
        If a number reappears and the index difference is <= k, we found a match.

        DRY RUN: nums = [1, 2, 3, 1], k = 3
        i=0, val=1: hash = {1:0}
        i=1, val=2: hash = {1:0, 2:1}
        i=2, val=3: hash = {1:0, 2:1, 3:2}
        i=3, val=1: 1 is in hash! (Current i:3 - Last i:0) = 3 <= k. Return True.
        """
        nums_hash = {} #value:index
        for i in range(len(nums)):
            if nums[i] in nums_hash:
                if (i - nums_hash[nums[i]]) <= k:
                    return True
            nums_hash[nums[i]] = i
        
        return False