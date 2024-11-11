class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                board[i][j] != word[k]):
                return False
            
            temp = board[i][j]
            board[i][j] = '#'  # mark as visited
            
            result = (dfs(i+1, j, k+1) or 
                      dfs(i-1, j, k+1) or 
                      dfs(i, j+1, k+1) or 
                      dfs(i, j-1, k+1))            
            board[i][j] = temp  # backtrack
            return result
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False