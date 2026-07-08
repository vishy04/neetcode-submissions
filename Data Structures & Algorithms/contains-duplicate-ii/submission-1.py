class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_hash = {} #value:index
        for i in range(len(nums)):
            if nums[i] in nums_hash:
                if (i - nums_hash[nums[i]]) <= k:
                    return True
            nums_hash[nums[i]] = i
        
        return False