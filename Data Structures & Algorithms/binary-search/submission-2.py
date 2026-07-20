class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums) - 1
        def condition(mid):
            return nums[mid] >= target

        while low < high:
            mid = low + (high-low)//2

            if condition(mid):
                high = mid
            else:
                low = mid + 1
        
        return low if nums[low] == target else -1
    
    