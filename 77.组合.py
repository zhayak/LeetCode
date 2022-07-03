#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def dfs(self, n, k, curr, start):
        if len(curr) == k:
            self.ans.append(curr[:])
        for i in range(start, n):
            self.dfs(n, k, curr + [i + 1], i + 1)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.dfs(n, k, [], 0)
        return self.ans

# @lc code=end

