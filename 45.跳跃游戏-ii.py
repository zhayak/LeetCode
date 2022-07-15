#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        farthest = 0
        next_far = 0
        cnt = 0
        i = 0
        while i <= farthest and i < len(nums):
            while i <= farthest and i < len(nums):
                next_far = max(next_far, i + nums[i])
                i += 1
            farthest = next_far
            cnt += 1
            if farthest >= len(nums) - 1:
                return cnt
        return 0

# @lc code=end

