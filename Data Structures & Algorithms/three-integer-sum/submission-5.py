class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = set()

        for i in range(n):

            j = i + 1
            k = n - 1
            
            while j < k :
                target = nums[i] + nums[j] + nums[k]
                if target > 0 :
                    k -= 1
                elif target < 0:
                    j += 1
                else :
                    temp = [nums[i], nums[j], nums[k]]
                    res.add(tuple(temp))
                    j += 1
                    k -= 1
        
        return [list(t) for t in res]