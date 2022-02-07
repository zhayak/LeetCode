# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''

        res = s[0]
        for i in range(1, n):
            j = i - 1
            while j >= 0 and i + (i-j) < n and s[j] == s[i + (i-j)]:
                j -= 1
            if i + (i-j-1) -j-1 + 1 > len(res):
                res = s[(j+1):(i + i-j)]
            j = i - 1
            while j >=0 and i + (i-j) - 1 < n and s[j] == s[i + (i-j) - 1]:
                j -= 1
            if i + (i-j-1) -j-1 > len(res):
                res = s[(j+1):(i + i-j-1)]
        return res
