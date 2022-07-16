class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = self.create_board(n)
        res = []
        self.helper(board,0,res)
        return res
        

    def isSafe(self, board, row, col):

        #check vertically
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        #check left diag
        for i in range(1, min(row,col) + 1):
            if board[row - i][col - i] == 'Q':
                return False

        #check right diag
        for i in range(1, min(row, len(board) - col - 1) + 1):
            if board[row - i][col + i] == 'Q':
                return False

        return True

    def helper(self, board, row, arr):
        #base condition
        if row == len(board):
            copy = [''.join(row) for row in board]
            arr.append(copy)
            return arr

        #new recusive calls
        for col in range(len(board)):
            if self.isSafe(board, row, col):
                board[row] = board[row][0:col] + 'Q' + board[row][col+1:]
                self.helper(board, row + 1, arr)
                board[row] = board[row][0:col] + '.' + board[row][col+1:]

    def create_board(self, n):
        board = []
        for i in range(n):
            s = ''
            for x in range(n):
                s =  s + '.'
            board.append(s)
        return board
