#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def dfs(self, nums, visited, curr, permutations):
        if len(nums) == len(curr):
            permutations.append(curr[:])
            return
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            curr.append(num)
            self.dfs(nums, visited, curr, permutations)
            visited.remove(num)
            curr.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        permutations = []
        self.dfs(nums, visited, [], permutations)
        return permutations

# @lc code=end

