#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def backtrack(self, digits, curr, i):
        if i == len(digits):
            self.ans.append(''.join(curr))
            return
        for ch in self.mapping[digits[i]]:
            self.backtrack(digits, curr + [ch], i + 1)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.ans = []
        self.mapping = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        self.backtrack(digits, [], 0)
        return self.ans

# @lc code=end

