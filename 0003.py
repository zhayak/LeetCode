# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        unique = set()
        right = 0
        n = len(s)
        for left in range(n):
            while right < n and s[right] not in unique:
                unique.add(s[right])
                right += 1
            unique.remove(s[left])
            res = max(right - left, res)

        return res
