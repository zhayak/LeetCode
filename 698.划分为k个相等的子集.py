#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def backtrack(self, nums, start, visited, curr, target, k):
        if k == 1:
            return True
        if curr == target:
            res = self.backtrack(nums, 0, visited, 0, target, k - 1)
            self.memo[str(visited)] = res
            return res
        if str(visited) in self.memo:
            return self.memo[str(visited)]
        for i in range(start, len(nums)):
            if visited[i] or nums[i] + curr > target:
                continue
            visited[i] = True
            curr += nums[i]
            if self.backtrack(nums, i + 1, visited, curr, target, k):
                return True
            curr -= nums[i]
            visited[i] = False
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        if max(nums) > target:
            return False
        visited = [False for i in range(len(nums))]
        self.memo = {}
        return self.backtrack(nums, 0, visited, 0, target, k)

# @lc code=end

