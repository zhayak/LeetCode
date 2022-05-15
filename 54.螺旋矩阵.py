#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        upper, lower, left, right = 0, m-1, 0, n-1
        res = []
        while len(res) < m * n:
            if upper <= lower:
                for i in range(left, right+1):
                    res.append(matrix[upper][i])
                upper += 1
            if left <= right:
                for i in range(upper, lower+1):
                    res.append(matrix[i][right])
                right -= 1
            if upper <= lower:
                for i in range(right, left-1, -1):
                    res.append(matrix[lower][i])
                lower -= 1
            if left <= right:
                for i in range(lower, upper-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
# @lc code=end

