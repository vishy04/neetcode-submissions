class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #we can have a answer > len(nums) if target > nums[-1] then we have to insert at the end
        # max(search_space) = len(nums) and not len(nums) - 1
        low , high = 0, len(nums)

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        #low gives me the smallest value >= target
        return low