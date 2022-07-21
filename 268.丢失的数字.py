#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
        
# @lc code=end

