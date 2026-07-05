class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        # add ground of height 0 at the end
        # heights.append(0) #avoids not empty stack problem at the end

        for idx, height in enumerate(heights):
            # we iterate through the heights to get right boundary
            # the element in consideration and left are in stack
            while stack and height < stack[-1][0]:
                h, j = stack.pop()  # this can make stack empty
                if stack:
                    area = (idx - (stack[-1][1] + 1)) * h
                else:  # curr_h spans till the start
                    area = (idx) * h
                max_area = max(area, max_area)

            stack.append((height, idx))

        while stack:
            h, j = stack.pop()  # this can make stack empty
            if stack:
                area = (len(heights) - (stack[-1][1] + 1)) * h
            else:  # curr_h is min and spans tills last
                area = (len(heights)) * h
            max_area = max(area, max_area)
        return max_area
