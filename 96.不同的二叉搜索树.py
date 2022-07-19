#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def helper(self, n):
        if n == 0 or n == 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        total = 0
        for i in range(1, n + 1):
            total += self.helper(i - 1) * self.helper(n - i)
        self.memo[n] = total
        return total
        
    def numTrees(self, n: int) -> int:
        self.memo = {}
        return self.helper(n)

# @lc code=end

