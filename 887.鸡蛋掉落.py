#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        f = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i][1] = i
        for j in range(1, k + 1):
            f[1][j] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
                if f[i][k] >= n:
                    return i
        return -1

# @lc code=end

