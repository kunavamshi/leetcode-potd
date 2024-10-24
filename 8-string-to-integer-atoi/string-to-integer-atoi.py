class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0
        
        # Initialize variables
        sign = 1
        result = 0
        index = 0
        n = len(s)
        
        # Check the sign of the number
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Convert the digits to an integer
        while index < n and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        # Apply the sign
        result *= sign
        
        # Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result