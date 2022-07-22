#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def twoSumClosest(self, nums, target):
        left, right = 0, len(nums) - 1
        closest = 10 ** 5
        ans = nums[0]
        while left < right:
            left_num = nums[left]
            right_num = nums[right]
            diff = left_num + right_num - target
            if abs(diff) < closest:
                ans = left_num + right_num
                closest = abs(diff)
            if left_num + right_num < target:
                while left < right and nums[left] == left_num:
                    left += 1
            elif left_num + right_num > target:
                while left < right and nums[right] == right_num:
                    right -= 1
            else:
                return target
        return ans

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        i = 0
        closest = 10 ** 5
        ans = 0
        while i < len(nums) - 2:
            num = nums[i]
            total = num + self.twoSumClosest(nums[(i + 1):], target - num)
            if abs(total - target) < closest:
                closest = abs(total - target)
                ans = total
            if closest == 0:
                return ans
            while i < len(nums) - 2 and nums[i] == num:
                i += 1
        return ans

# @lc code=end

