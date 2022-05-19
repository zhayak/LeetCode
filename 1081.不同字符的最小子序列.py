#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        stack = []
        for ch in s:
            counter[ch] -= 1
            if ch in stack:
                continue
            while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)

# @lc code=end

