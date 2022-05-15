#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for j in range(n)] for i in range(n)]
        upper, lower, left, right = 0, n-1, 0, n-1
        cnt = 1
        while cnt <= n * n:
            if upper <= lower:
                for j in range(left, right+1):
                    res[upper][j] = cnt
                    cnt += 1
                upper += 1
            if left <= right:
                for i in range(upper, lower+1):
                    res[i][right] = cnt
                    cnt += 1
                right -= 1
            if upper <= lower:
                for j in range(right, left-1, -1):
                    res[lower][j] = cnt
                    cnt += 1
                lower -= 1
            if left <= right:
                for i in range(lower, upper-1, -1):
                    res[i][left] = cnt
                    cnt += 1
                left += 1
        return res
# @lc code=end

