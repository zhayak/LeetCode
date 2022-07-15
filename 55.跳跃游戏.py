#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        i = 0
        while i <= farthest and i < len(nums):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
            i += 1
        return False

# @lc code=end

