#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 == 1:
            return 0
        m = (total + target) // 2
        n = len(nums)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(m + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[n][m]

# @lc code=end

