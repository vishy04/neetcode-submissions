class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize three boundary counters: zero, one, and two.
        # These track the upper bound index for each respective number.
        # - If we see 0: Shift all three boundaries.
        # - If we see 1: Shift the boundaries for 1 and 2.
        # - If we see 2: Shift only the boundary for 2.
        zero = one = two = 0

        for num in nums:
            if num == 0:
                zero += 1
                one += 1
                two += 1
            elif num == 1:
                one += 1
                two += 1
            else:
                two += 1
        
        # Overwrite the original array using the calculated boundaries
        for i in range(zero):
            nums[i] = 0
        for i in range(zero, one):
            nums[i] = 1
        for i in range(one, len(nums)):
            nums[i] = 2