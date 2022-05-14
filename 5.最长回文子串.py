#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0
        for i in range(len(s)):
            left = i
            right = i + (i - left)
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        res = s[left:(right + 1)]
                    left -= 1
                    right += 1
                else:
                    break
            left = i
            right = i + (i - left) - 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        res = s[left:(right + 1)]
                    left -= 1
                    right += 1
                else:
                    break
        return res

# @lc code=end

