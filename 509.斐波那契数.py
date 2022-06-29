#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        l1 = 0
        l2 = 1
        for i in range(n-1):
            ans = l1 + l2
            l1 = l2
            l2 = ans
        return ans

# @lc code=end

