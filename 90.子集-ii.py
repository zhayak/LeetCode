#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def dfs(self, nums, start, curr, visited):
        self.ans.append(curr)
        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                continue
            visited.add(i)
            self.dfs(nums, i + 1, curr + [nums[i]], visited)
            visited.remove(i)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        visited = set()
        nums = sorted(nums)
        self.dfs(nums, 0, [], visited)
        return self.ans

# @lc code=end

