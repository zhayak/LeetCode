#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def isFeasible(self, nums: List[int], m: int, target: int) -> bool:
        cnt = 1
        curr = 0
        for num in nums:
            if curr + num <= target:
                curr += num
            else:
                cnt += 1
                curr = num
        return cnt <= m
    
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.isFeasible(nums, m, mid):
                right = mid
            else:
                left = mid
        if self.isFeasible(nums, m, left):
            return left
        else:
            return right

# @lc code=end

