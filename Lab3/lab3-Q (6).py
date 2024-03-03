class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp_divisor, power_of_two = divisor, 1
            while dividend >= temp_divisor << 1:
                temp_divisor <<= 1
                power_of_two <<= 1
            
            dividend -= temp_divisor
            result += power_of_two

        return -result if negative else min(result, 2**31 - 1)
