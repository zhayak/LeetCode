#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        from random import randint
        presum = [0 for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):
            presum[i] = presum[i - 1] + w[i - 1]
        self.presum = presum

    def pickIndex(self) -> int:
        randidx = randint(1, self.presum[-1])
        left, right = 0, len(self.presum) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.presum[mid] >= randidx:
                right = mid
            else:
                left = mid
        if self.presum[left] >= randidx:
            return left - 1
        else:
            return right - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

