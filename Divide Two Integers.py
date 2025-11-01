class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine if result should be negative
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Subtract divisor multiples using bit shifts
        for i in range(31, -1, -1):
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                quotient += 1 << i

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp to 32-bit integer range
        return max(min(quotient, INT_MAX), INT_MIN)
