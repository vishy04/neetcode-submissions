class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #pair (temp , index)

        for i , temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stackT , stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            #default
            stack.append((temp,i))
        
        return result