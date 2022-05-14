#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        while curr < len(nums) and nums[curr] != 0:
            curr += 1
        for i in range(curr, len(nums)):
            if nums[i] != 0:
                nums[curr] = nums[i]
                nums[i] = 0
                curr += 1

# @lc code=end

