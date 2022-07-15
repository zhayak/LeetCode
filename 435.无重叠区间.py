#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        cnt = 0
        i = 0
        while i < len(intervals):
            curr = intervals[i]
            i += 1
            while i < len(intervals) and intervals[i][0] < curr[1]:
                cnt += 1
                i += 1
        return cnt

# @lc code=end

