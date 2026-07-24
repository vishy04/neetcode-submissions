class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Revision ( 24 July : 1 Hour): No Help Solution 
        """
        This approach uses a monotonic increasing stack to track the left boundaries 
        of potential rectangles. By iterating through the heights, any height smaller 
        than the top of the stack acts as a right boundary for the taller bars. 
        When this occurs, the taller bars are popped from the stack, and their 
        areas are calculated using the current index as the right boundary and the 
        new stack top as the left boundary.
        """
        # Append 0 as a sentinel value to ensure the stack is fully emptied at the end
        heights.append(0)
        
        stack = []  # Stores tuples of (height, index)
        max_area = 0
        
        for right_boundary, height in enumerate(heights):
            # If current height is less than the last height, we found a right boundary
            while stack and height < stack[-1][0]:
                curr_height, i = stack.pop()
                
                # If stack has remaining elements, the new top is the left boundary
                if stack:
                    area = (right_boundary - (stack[-1][1] + 1)) * curr_height
                else:
                    # If stack is empty, the rectangle extends all the way to index 0
                    area = right_boundary * curr_height
                    
                max_area = max(max_area, area)
            
            stack.append((height, right_boundary))

        return max_area