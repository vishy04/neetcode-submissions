class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sorting
        nums.sort()
        #calculating the length for iteration 
        n = len(nums)
        #result in set for eliminating duplicate -> convert to list[list] later
        res = []
        #working loop
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1,n):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i],nums[j],nums[k]])
        #coverting every element of res set-> tuple to list()
        #and returning a list of those elements
        return res