class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n==0:
            return 1.00
        
        if n < 0 :
            x = 1.0/x
            n = -n
        
        result = 1.00
        """
        for n even (x^2)^(n//2)
        for n odd  x.(x^2)^(n//2)
        """
        while n > 0:
            
            if n%2 == 1:
                result *= x

            x *= x
            n //= 2
        return result