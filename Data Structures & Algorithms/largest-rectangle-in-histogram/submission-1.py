class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        INTUITION: Monotonic Increasing Stack
        To calculate the maximum area a specific bar can support, we need to find 
        its left and right boundaries (the nearest smaller bars on both sides).
        - Right boundary: Found when we encounter a new bar shorter than the stack's top.
        - Left boundary: The element sitting directly beneath it in the stack.
        """
        
        # Stack stores tuples of: (height, index)
        stack = []  
        max_area = 0
        
        # Append 0 to act as a universal right boundary.
        # Without this, bars that can extend all the way to the end of the array 
        # would be left stuck in the stack, and their areas would never be calculated.
        heights.append(0)
        
        for index, height in enumerate(heights):
            
            # When we hit a shorter bar, we have found the right boundary 
            # for the taller bars currently sitting at the top of the stack.
            while stack and stack[-1][0] >= height:
                popped_height, j = stack.pop()  
                
                # After popping, the NEW top of the stack is the left boundary 
                # (the nearest smaller bar to the left of the popped bar).
                if stack:
                    width = index - (stack[-1][1] + 1)
                
                # If the stack is empty, it means no smaller bar exists to the left.
                # The popped bar can extend all the way back to the start (index 0).
                else:  
                    width = index - 0
                    
                max_area = max(max_area, popped_height * width)
                
            stack.append((height, index))

        return max_area