class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        #Sorting
        nums.sort()
        count = 1
        max_count = 1
        #checking if consecutive
        for i in range(1, len(nums)):
            #skipping the duplicate
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i-1] + 1 :
                count += 1
            else :
                #sequence broken , update max_count
                max_count = max(max_count , count)
                count = 1
        #if the largest sequence end on the last element,
        # the max_count will not get updated 
        return max(max_count, count)