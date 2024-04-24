class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize an array to store previously calculated Tribonacci numbers
        tribonacci_nums = [0] * (n + 1)
        tribonacci_nums[1] = 1
        tribonacci_nums[2] = 1
        
        # Calculate Tribonacci numbers iteratively
        for i in range(3, n + 1):
            tribonacci_nums[i] = tribonacci_nums[i - 1] + tribonacci_nums[i - 2] + tribonacci_nums[i - 3]
        
        return tribonacci_nums[n]

# Test cases
solution = Solution()
print(solution.tribonacci(4))  # Output: 4
print(solution.tribonacci(25)) # Output: 1389537