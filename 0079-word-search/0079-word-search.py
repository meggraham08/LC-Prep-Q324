from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(r, c, index):
            row_inbounds = 0 <= r < m
            col_inbounds = 0 <= c < n
            if not row_inbounds or not col_inbounds or board[r][c] != word[index] or (r, c) in visited:
                return False
            if index == len(word) - 1:
                return True
            visited.add((r,c))
            found = False
            for dr, dc in [(1,0), (-1, 0), (0,1), (0,-1)]:
                if dfs(r+dr, c + dc, index + 1):
                    return True

            visited.remove((r, c))
            return False
        
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False


