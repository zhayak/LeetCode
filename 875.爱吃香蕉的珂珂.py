#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def calcHours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for pile in piles:
            hours += pile // speed + 1 if pile % speed > 0 else pile // speed
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.calcHours(piles, mid) > h:
                left = mid
            else:
                right = mid
        if self.calcHours(piles, left) <= h:
            return left
        else:
            return right

# @lc code=end

