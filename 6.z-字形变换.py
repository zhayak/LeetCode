#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        row = 0
        direction = 1
        for i in range(len(s)):
            ans[row].append(s[i])
            row += direction
            if row < 0 or row >= numRows:
                direction *= -1
                row += 2 * direction
        return ''.join([''.join(_) for _ in ans])

# @lc code=end

