class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # because 1 <= nums[i] <= len(nums)
        # we can use marking based on index
        nums_len = len(nums)
        for i in range(nums_len):
            # index with value nums[i]
            value = abs(nums[i])
            if nums[value - 1] < 0:
                return value
            nums[value - 1] *= -1
