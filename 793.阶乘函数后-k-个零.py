#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start
class Solution:
    def calcZero(self, n):
        cnt = 0
        divisor = 5
        while divisor <= n:
            cnt += n // divisor
            divisor *= 5
        return cnt

    def preimageSizeFZF(self, k: int) -> int:
        left, right = 0, 10 ** 10
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.calcZero(mid) <= k:
                left = mid
            else:
                right = mid
        if self.calcZero(right) == k:
            right_bound = right
        else:
            right_bound = left
        
        left, right = 0, 10 ** 10
        while left + 1 <right:
            mid = left + (right - left) // 2
            if self.calcZero(mid) >= k:
                right = mid
            else:
                left = mid
        if self.calcZero(left) == k:
            left_bound = left
        else:
            left_bound = right
        
        return right_bound - left_bound + 1

# @lc code=end

