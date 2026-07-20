class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Revision ( Fri 21 Jul )
        def condition(mid:int) -> bool:
            return nums[mid] >= target
        
        low , high = 0 , len(nums) # not len - 1 as last position can also be an answer

        while low < high:
            mid = low + (high - low) // 2

            if condition(mid):
                high = mid
            else :
                low = mid + 1
        
        return low