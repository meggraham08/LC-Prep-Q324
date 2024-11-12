from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Check if we've matched all characters in the word
            if index == len(word):
                return True
            # Check out of bounds, mismatch, or already visited cell
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited by temporarily changing its value
            temp, board[r][c] = board[r][c], '#'
            
            # Explore neighbors in the four cardinal directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Unmark the cell (backtrack) by restoring its original value
            board[r][c] = temp
            return found

        # Start DFS from each cell on the board
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
