class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        result = []
        length = len(temperatures)
        for i in range(length):
            indicator = 0
            for j in range(i+1 , length):
                if temperatures[i] < temperatures[j]:
                    result.append(j-i)
                    indicator = 1
                    break
            if indicator == 0:
                result.append(0)
                    
        
        return result
                