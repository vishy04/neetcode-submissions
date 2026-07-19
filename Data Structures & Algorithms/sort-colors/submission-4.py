class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Apply DNF Solution
        """
        low = mid = 0 
        high = len(nums) - 1

        while mid <= high: 
            if nums[mid] == 0 :
                nums[mid] , nums[low] = nums[low] , nums[mid]
                #we can move mid here because we know that all the numbers till mid and low are seen
                mid += 1 
                low += 1
            elif nums[mid] == 2 :
                nums[mid] , nums[high] = nums[high], nums[mid]
                high -= 1 #we do not need to move mid , as we do not know which number came from high
            else:
                mid += 1
        
        