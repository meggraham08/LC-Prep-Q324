from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, index):
            # Check row and column bounds
            row_inbounds = 0 <= r < m
            col_inbounds = 0 <= c < n
            
            # If out of bounds, character mismatch, or cell already visited, return False
            if not row_inbounds or not col_inbounds or board[r][c] != word[index] or (r, c) in visited:
                return False
            
            # If all characters are matched, return True
            if index == len(word) - 1:
                return True
            
            # Mark the cell as visited by adding to the visited set
            visited.add((r, c))
            
            # Explore neighbors in the four cardinal directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Unmark the cell (backtrack) by removing from visited
            visited.remove((r, c))
            return found

        # Start DFS from each cell on the board
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
