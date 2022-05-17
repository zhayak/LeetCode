#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_dict = defaultdict(int)
        left, right = 0, 0
        max_len = 0
        valid = True
        while right < len(s):
            ch = s[right]
            right += 1
            window_dict[ch] += 1
            while window_dict[ch] > 1:
                ch2 = s[left]
                left += 1
                window_dict[ch2] -= 1
            if right - left > max_len:
                max_len = right - left
        return max_len

# @lc code=end

