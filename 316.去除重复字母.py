#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        stack = []
        for ch in s:
            count[ch] -= 1
            if ch in stack:
                continue
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)

# @lc code=end

