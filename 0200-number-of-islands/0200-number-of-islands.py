class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, visited) == True:
                    count += 1
        return count

    def dfs(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])

        if not row_inbounds or not col_inbounds or grid[r][c] == '0' or (r,c) in visited:
            return False
        visited.add((r,c))
        
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r , c - 1, visited)
        self.dfs(grid, r, c + 1, visited)
        return True
