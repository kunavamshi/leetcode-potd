class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def trib(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = trib(n - 1) + trib(n - 2) + trib(n - 3)
                memo[n] = result
                return result
        
        return trib(n)

# Test cases
solution = Solution()
print(solution.tribonacci(4))  # Output: 4
print(solution.tribonacci(25)) # Output: 1389537