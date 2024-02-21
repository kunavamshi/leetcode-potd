class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

# Test cases
sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))              
print(sol.rangeBitwiseAnd(0, 0))              
print(sol.rangeBitwiseAnd(1, 2147483647))      

        