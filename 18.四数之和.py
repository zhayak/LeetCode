#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = list(sorted(nums))
        i = 0
        while i < len(nums) - 3:
            ans_three = self.threeSum(nums[(i + 1):], target - nums[i])
            if len(ans_three) > 0:
                ans += [[nums[i]] + _ for _ in ans_three]
            while i < len(nums) - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans

    def threeSum(self, nums, target):
        ans = []
        i = 0
        while i < len(nums) - 2:
            ans_two = self.twoSum(nums[(i + 1):], target - nums[i])
            if len(ans_two) > 0:
                ans += [[nums[i]] + _ for _ in ans_two]
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans

    def twoSum(self, nums, target):
        ans = []
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                ans.append([nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
        return ans

# @lc code=end

