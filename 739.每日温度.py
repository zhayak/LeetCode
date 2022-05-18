#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            res[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)
        return res

'''
class Solution:
    def dailyTemperatures(self, temperatures):
        if not temperatures:
            return [0]
        n = len(temperatures)
        stack = []
        results = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return results
'''
# @lc code=end

