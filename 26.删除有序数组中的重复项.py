#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        curr = 0
        for i in range(len(nums)):
            if nums[curr] != nums[i]:
                curr += 1
                nums[curr] = nums[i]
        return curr + 1

# @lc code=end

