#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
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
            self.cnt += 1
            return
        for col in range(len(board)):
            if not self.isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.cnt

# @lc code=end

