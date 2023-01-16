#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n):
            if (n - i) < m or haystack[i] != needle[0]:
                continue
            if haystack[i:(i + m)] == needle:
                return i
        return -1

# @lc code=end

