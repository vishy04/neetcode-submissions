class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[left],heights[right])
            if area > max_area:
                max_area = area
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else :
                left += 1
                right -= 1
        
        return max_area