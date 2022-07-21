#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        divisor = 5
        while divisor <= n:
            cnt += n // divisor
            divisor *= 5
        return cnt
        
# @lc code=end

