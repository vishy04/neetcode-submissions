class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        INTUITION: Two Pointers
        Since the array is sorted, all duplicate elements are grouped together (adjacent).
        We can use two pointers:
        - 'left' tracks the position where the NEXT unique element should be written.
        - 'right' scans ahead to find the next unique element.
        """
        
        left = right = 0
        nums_length = len(nums)
        
        while right < nums_length:
            # Step 1: Overwrite the next available position with the current unique element
            nums[left] = nums[right]
            
            # Step 2: Fast-forward 'right' past all duplicates of the element we just placed
            while right < nums_length and nums[right] == nums[left]:
                right += 1
                
            # Step 3: Advance 'left' to prepare for the next unique element
            left += 1
            
        return left 
        
        """
        DRY RUN:
        nums = [2, 10, 10, 30, 30, 30]  (Array must be sorted)
        
        Init: left = 0, right = 0
        Iter 1: nums[0] = nums[0] (2).  'right' skips to index 1. left=1, right=1.
        Iter 2: nums[1] = nums[1] (10). 'right' skips both 10s. left=2, right=3.
        Iter 3: nums[2] = nums[3] (30). 'right' skips all 30s.  left=3, right=6.
        
        End: right(6) == nums_length. Return left(3).
        Result: [2, 10, 30, ...]
        """