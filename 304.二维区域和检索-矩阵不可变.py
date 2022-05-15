#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        presum = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] + matrix[i][j] - presum[i][j]
        self.presum = presum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row1][col2+1] - self.presum[row2+1][col1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

