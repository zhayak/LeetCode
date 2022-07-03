#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def backtrack(self, board, word, curr, visited, row, col):
        if curr == len(word):
            return True
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x = row + dx
            y = col + dy
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                continue
            if (x, y) in visited or board[x][y] != word[curr]:
                continue
            visited.add((x, y))
            if self.backtrack(board, word, curr + 1, visited, x, y):
                return True
            visited.remove((x, y))
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if self.backtrack(board, word, 1, visited, i, j):
                        return True
        return False

# @lc code=end

