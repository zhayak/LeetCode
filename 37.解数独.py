#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def backtrack(self, board, row, col, visited_row, visited_col, visited_grid):
        if col == 9:
            return self.backtrack(board, row + 1, 0, visited_row, visited_col, visited_grid)
        if row == 9:
            return True
        if board[row][col] != '.':
            return self.backtrack(board, row, col + 1, visited_row, visited_col, visited_grid)
        for i in range(1, 10):
            if i in visited_row[row] or i in visited_col[col] or i in visited_grid[row // 3][col // 3]:
                continue
            visited_row[row].add(i)
            visited_col[col].add(i)
            visited_grid[row // 3][col // 3].add(i)
            board[row][col] = str(i)
            if self.backtrack(board, row, col + 1, visited_row, visited_col, visited_grid):
                return True
            visited_row[row].remove(i)
            visited_col[col].remove(i)
            visited_grid[row // 3][col // 3].remove(i)
            board[row][col] = '.'
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited_row = [set() for _ in range(9)]
        visited_col = [set() for _ in range(9)]
        visited_grid = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                visited_row[i].add(num)
                visited_col[j].add(num)
                visited_grid[i // 3][j // 3].add(num)
        self.backtrack(board, 0, 0, visited_row, visited_col, visited_grid)

# @lc code=end

