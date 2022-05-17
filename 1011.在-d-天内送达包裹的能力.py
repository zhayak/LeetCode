#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def calcDays(self, weights: List[int], capacity: int) -> int:
        days = 1
        curr = 0
        for weight in weights:
            if curr + weight <= capacity:
                curr += weight
            else:
                days += 1
                curr = weight
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.calcDays(weights, mid) > days:
                left = mid
            else:
                right = mid
        if self.calcDays(weights, left) <= days:
            return left
        else:
            return right

# @lc code=end

