#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        end = 0
        cnt = 0
        for s, e in intervals:
            if e > end:
                cnt += 1
                end = e
        return cnt

# @lc code=end

