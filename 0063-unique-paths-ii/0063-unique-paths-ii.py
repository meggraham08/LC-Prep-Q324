from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        memo = {}
        m , n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n or grid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in memo:
                return memo[(r,c)]
            paths = dfs(r+1, c) + dfs(r, c + 1)
            memo[(r,c)] = paths
            return paths
        return dfs(0,0)

            