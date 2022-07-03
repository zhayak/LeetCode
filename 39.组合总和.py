#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def backtrack(self, nums, start, total, curr, target):
        if total == target:
            self.ans.append(curr[:])
        if total > target:
            return
        for i in range(start, len(nums)):
            total += nums[i]
            self.backtrack(nums, i, total, curr + [nums[i]], target)
            total -= nums[i]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(candidates)
        self.backtrack(nums, 0, 0, [], target)
        return self.ans

# @lc code=end

