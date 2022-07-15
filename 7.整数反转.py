#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = x // abs(x)
        x = abs(x)
        ans = 0
        while x > 0:
            digit = x % 10
            x = x // 10
            ans = ans * 10 + digit
        return sign * ans if -2**31 <= sign * ans <= 2**31 - 1 else 0

# @lc code=end

