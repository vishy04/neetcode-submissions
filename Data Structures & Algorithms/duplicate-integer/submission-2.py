class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_dict = {}

        for num in nums:
            if num in hash_dict:
                return True 
            
            hash_dict[num] = 1

        return False
        








