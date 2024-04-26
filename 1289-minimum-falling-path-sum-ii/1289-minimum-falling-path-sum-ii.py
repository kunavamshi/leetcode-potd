from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        
        # Initialize the first row of dp
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        # Iterate over the rows of grid
        for i in range(1, n):
            # Iterate over the columns of grid
            for j in range(n):
                # Find the minimum value from the previous row's cells that are not in the same column
                min_prev = min(dp[i-1][c] for c in range(n) if c != j)
                dp[i][j] = grid[i][j] + min_prev
        
        # Return the minimum value from the last row of dp
        return min(dp[-1])

# Test the function
grid1 = [[1,2,3],[4,5,6],[7,8,9]]
grid2 = [[7]]

ob = Solution()
print(ob.minFallingPathSum(grid1))  # Output: 13
print(ob.minFallingPathSum(grid2))  # Output: 7