#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def dfs(self, nums, target, start, curr, total):
        if total == target:
            self.ans.append(curr[:])
        if total > target:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            total += nums[i]
            self.dfs(nums, target, i + 1, curr + [nums[i]], total)
            total -= nums[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(candidates)
        self.dfs(nums, target, 0, [], 0)
        return self.ans

# @lc code=end

