class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        #nums[j] + nums[k] == -nums[i]
        res = []
        for i in range(n):
            #skipping duplicate for selected number nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue #skips iteration 
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k :
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # make pointer move ahead
                    j += 1
                    #skipping duplicate for j 
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    # #skipping duplicate for k 
                    # while j < k and nums[k] == nums[k-1]:
                    #     k += 1
                    

        return res