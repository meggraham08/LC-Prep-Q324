from collections import deque
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def can_reach(threshold):
            visited = set()
            stack = [(0, 0)]
            
            while stack:
                x, y = stack.pop()
                if x == rows - 1 and y == cols - 1:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] >= threshold:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
            return False
        
        left, right = 0, min(grid[0][0], grid[-1][-1])
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1  
        return result
            