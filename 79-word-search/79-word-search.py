class Solution:
    def exist(self, board, word):
        
        if len(word) > len(board) * len(board[0]):
            return False;
        
        if len(board)*len(board[0]) == 1:
            if board[0][0] == word:
                return True
        
        try:
            visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
            for j in range(0, len(board[0])):
                for i in range(0, len(board)):
                    if board[i][j] == word[0]:
                        self.backtrack(i, j, board,visited, word)
        except Exception as e:
            return True
        return False

    def backtrack(self, r, c, board,visited, word):
        if len(word) == 0:
            raise Exception("Tru")

        if visited[r][c]:
            return

        visited[r][c] = True

        if r < len(board) - 1 and board[r][c] == word[0]:
            self.backtrack(r + 1, c, board,visited, word[1:])

        if c < len(board[0]) - 1 and board[r][c] == word[0]:
            self.backtrack(r, c + 1, board,visited, word[1:])

        if c > 0 and board[r][c] == word[0]:
            self.backtrack(r, c - 1, board,visited, word[1:])

        if r > 0 and board[r][c] == word[0]:
            self.backtrack(r - 1, c, board,visited, word[1:])

        visited[r][c] = False
