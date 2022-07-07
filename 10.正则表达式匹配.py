#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        i, j = 0, 0
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m][n]

# @lc code=end

