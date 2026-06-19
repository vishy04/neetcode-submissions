class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sorting
        nums.sort()
        #calculating the length for iteration 
        n = len(nums)
        #result in set for eliminating duplicate -> convert to list[list] later
        res = set()
        #working loop
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        
        return [list(i) for i in res]