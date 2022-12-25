#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        res = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            res = max(res, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

# @lc code=end

