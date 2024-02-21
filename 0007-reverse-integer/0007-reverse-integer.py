class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1
        x = abs(x)
        reversed_x = int(str(x)[::-1])
        
        if reversed_x > 2**31 - 1:
            return 0
        
        return sign * reversed_x