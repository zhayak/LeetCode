#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        ans = []
        n = len(nums) - 1
        left, right = 0, n
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                curr = nums[left]
                while left < right and nums[left] == curr:
                    left += 1
            elif total > target:
                curr = nums[right]
                while left < right and nums[right] == curr:
                    right -= 1
            else:
                ans.append([nums[left], nums[right]])
                curr = nums[left]
                while left < right and nums[left] == curr:
                    left += 1
                curr = nums[right]
                while left < right and nums[right] == curr:
                    right -= 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0
        while i < len(nums):
            num = nums[i]
            two_ans = self.twoSum(nums[(i + 1):], -num)
            ans += [[num] + _ for _ in two_ans]
            while i < len(nums) and nums[i] == num:
                i += 1
        return ans

# @lc code=end

