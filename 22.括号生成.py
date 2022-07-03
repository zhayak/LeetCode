#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def backtrack(self, curr, left, right):
        if left == 0 and right == 0:
            self.ans.append(''.join(curr))
        if left > 0:
            self.backtrack(curr + ["("], left - 1, right)
        if right > left:
            self.backtrack(curr + [")"], left, right - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack([], n, n)
        return self.ans
        
# @lc code=end

