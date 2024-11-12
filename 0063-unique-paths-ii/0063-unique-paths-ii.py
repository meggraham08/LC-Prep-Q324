from typing import List

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        memo = {}
        # size of board
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            # Position out of bounds or hit an obstacle
            if r >= m or c >= n or grid[r][c] == 1:
                return 0
            # If we reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                return 1
            # Check if result already computed for this position
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Calculate paths from the current cell
            paths = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = paths  # Store the result in memo
            return paths

        return dfs(0, 0)
