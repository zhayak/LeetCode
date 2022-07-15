#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s is None or len(s) == 0:
            return 0
        
        ans = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for ch in s:
            if not '0' <= ch <= '9':
                break
            ans = ans * 10 + int(ch)
        ans = ans * sign
        ans = min(max(ans, -2**31), 2**31 - 1)
        return ans

# @lc code=end

