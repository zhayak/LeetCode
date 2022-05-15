#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        window_dict = defaultdict(int)
        for ch in t:
            t_dict[ch] += 1

        left, right = 0, 0
        valid = 0
        min_len = len(s) + 1
        res = ""
        while right < len(s):
            ch = s[right]
            right += 1
            if ch in t_dict:
                window_dict[ch] += 1
                if window_dict[ch] == t_dict[ch]:
                    valid += 1
            
            while valid == len(t_dict):
                if right - left < min_len:
                    min_len = right - left
                    res = s[left:right]
                ch = s[left]
                left += 1
                if ch in t_dict:
                    if window_dict[ch] == t_dict[ch]:
                        valid -= 1
                    window_dict[ch] -= 1
        return res
        

# @lc code=end

