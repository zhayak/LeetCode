#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        start, end = intervals[0]
        ans = []
        for s, e in intervals:
            if s <= end:
                end = max(end, e)
            else:
                ans.append([start, end])
                start = s
                end = e
        ans.append([start, end])
        return ans

# @lc code=end

