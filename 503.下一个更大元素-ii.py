#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1 for _ in range(n * 2)]
        for i in range(n * 2):
            while stack and nums[stack[-1] % n] < nums[i % n]:
                res[stack[-1]] = nums[i % n]
                stack.pop()
            stack.append(i)
        return res[:n]

# @lc code=end

