#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        window_dict = defaultdict(int)
        for ch in s1:
            s1_dict[ch] += 1
        valid, target = 0, len(s1_dict)
        left, right = 0, 0
        while right < len(s2):
            ch = s2[right]
            right += 1
            if ch in s1_dict:
                window_dict[ch] += 1
                if window_dict[ch] == s1_dict[ch]:
                    valid += 1
            while (right - left) >= len(s1):
                if valid == target:
                    return True
                ch = s2[left]
                left += 1
                if ch in s1_dict:
                    if window_dict[ch] == s1_dict[ch]:
                        valid -= 1
                    window_dict[ch] -= 1
        return False

# @lc code=end

