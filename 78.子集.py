#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def dfs(self, nums, start, curr):
        self.ans.append(curr)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, curr + [nums[i]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.dfs(nums, 0, [])
        return self.ans

# @lc code=end

