#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = defaultdict(int)
        window_dict = defaultdict(int)
        for ch in p:
            p_dict[ch] += 1
        left, right = 0, 0
        valid, target = 0, len(p_dict)
        res = []
        
        while right < len(s):
            ch = s[right]
            right += 1
            if ch in p_dict:
                window_dict[ch] += 1
                if window_dict[ch] == p_dict[ch]:
                    valid += 1
            while (right - left) >= len(p):
                if valid == target:
                    res.append(left)
                ch = s[left]
                left += 1
                if ch in p_dict:
                    if window_dict[ch] == p_dict[ch]:
                        valid -= 1
                    window_dict[ch] -= 1
        return res 

# @lc code=end

