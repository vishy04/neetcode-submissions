class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #dict : index -> values
        hash = {}

        for index , num in enumerate(nums):
            if num in hash.keys():
                if abs(hash[num] - index)<= k:
                    return True
            hash[num] = index
        return False

