class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark the current cell as visited
            dfs(grid, i+1, j)  # Visit the cell below
            dfs(grid, i-1, j)  # Visit the cell above
            dfs(grid, i, j+1)  # Visit the cell to the right
            dfs(grid, i, j-1)  # Visit the cell to the left
        
        if not grid:
            return 0
        
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)  # Explore the island using DFS
        return num_islands