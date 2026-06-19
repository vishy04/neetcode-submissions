class Solution:
    def trap(self, height: List[int]) -> int:
        #look at the video of greg hogg
        n = len(height)
        """
        precomputing the left_max and right_max
        at every position 
        area at every position = min(left,right) - current(height)
        """

        left_max = [0] * n 
        right_max = [0] * n 

        #calculating left_max start and end = 0 wall water will fall
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
            
        right_max[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
        area = 0
        for i in range(n):
            potential_area = min(left_max[i],right_max[i]) - height[i]
            area += potential_area#for positive


        return area
