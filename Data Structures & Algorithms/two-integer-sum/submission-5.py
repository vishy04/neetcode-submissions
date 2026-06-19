class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_dict = {}  # val->index



        for i, num in enumerate(nums) :
            diff = target - num 
            #check for same element twice when doing two pass
            if diff in hash_dict :
                return [hash_dict[diff], i]
            hash_dict[num] = i

        return [] 
