class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Eg: [1,0,1,2]
        count = [0,0,0] # index -> freq

        for num in nums:
            count[num] += 1
        #count = [1,2,1]
        
        #iterate over 
        running_index = 0
        for i in range(3):
            occurence = count[i]
            while occurence:
                nums[running_index] = i
                occurence -= 1
                running_index += 1

        
        # [0,1,1,2]
        

        