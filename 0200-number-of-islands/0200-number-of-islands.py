class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
              
        count = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Start a DFS only if the cell is land and hasn't been visited
                if grid[r][c] == '1' and (r, c) not in visited:
                    self.dfs(grid, r, c, visited)
                    count += 1  # New island found
        
        return count
    
    def dfs(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        
        # If out of bounds, water, or already visited, stop the DFS for this path
        if not row_inbounds or not col_inbounds or grid[r][c] == '0' or (r, c) in visited:
            return
        
        # Mark the cell as visited
        visited.add((r, c))
        
        # Visit all 4 neighbors (up, down, left, right)
        self.dfs(grid, r - 1, c, visited)  # Up
        self.dfs(grid, r + 1, c, visited)  # Down
        self.dfs(grid, r, c - 1, visited)  # Left
        self.dfs(grid, r, c + 1, visited)  # Right