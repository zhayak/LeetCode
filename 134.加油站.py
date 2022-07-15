#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        total = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

# @lc code=end

