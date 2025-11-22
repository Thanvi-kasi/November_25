class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Fast power (binary exponentiation)
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        base = x
        
        while n > 0:
            if n & 1:          # If lowest bit is 1
                result *= base
            base *= base       # Square the base
            n >>= 1            # Shift exponent right
        
        return result
