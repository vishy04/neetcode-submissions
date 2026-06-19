class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1 :
            return nums[0]

        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1
                if count > n // 2:
                    return nums[i]
            
        
        return 0