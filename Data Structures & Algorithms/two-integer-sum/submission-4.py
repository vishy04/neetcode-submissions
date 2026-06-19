class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_dict = {}  # val->index

        for idx, val in enumerate(nums):
            hash_dict[val] = idx

        for i, num in enumerate(nums) :
            diff = target - num 
            #check for same element twice when doing two pass
            if diff in hash_dict and hash_dict[diff] != i:
                return [i, hash_dict[diff]]

        return [] 
