#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def isValid(self, board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    
    def backtrack(self, board, row):
        if row == len(board):
            self.ans.append([''.join(row) for row in board])
            return
        for col in range(len(board)):
            if not self.isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.ans = []
        self.backtrack(board, 0)
        return self.ans

# @lc code=end

