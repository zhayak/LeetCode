#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def dfs(self, nums, curr, visited, permutations):
        if len(curr) == len(nums):
            permutations.append(curr[:])
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                continue
            visited.add(i)
            curr.append(nums[i])
            self.dfs(nums, curr, visited, permutations)
            visited.remove(i)
            curr.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        permutations = []
        nums = sorted(nums)
        self.dfs(nums, [], visited, permutations)
        return permutations

# @lc code=end

