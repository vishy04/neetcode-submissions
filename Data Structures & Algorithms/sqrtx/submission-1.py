class Solution:
    def mySqrt(self, x: int) -> int:
        #base condition root 1 is number itself
        if x == 1:
            return 1
        
        left, right = 1 , x

        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x: #condition
                right = mid
            else:
                left = mid + 1
        # left gives the minimum value where mid * mid > x( Condition )
        return left - 1    
    