class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        size = 0
        max_size = float('-inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.dfs(grid, r, c, visited)
                if size > max_size:
                    max_size = size
        return max_size

    def dfs(self, grid, r, c, visited):
        pos = (r, c)
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds or grid[r][c] == 0 or pos in visited:
            return 0
        visited.add(pos)
        size = 1

        size += self.dfs(grid, r + 1, c, visited)
        size += self.dfs(grid, r - 1, c, visited)
        size += self.dfs(grid, r , c + 1, visited)
        size += self.dfs(grid, r, c - 1, visited)
        return size         


 