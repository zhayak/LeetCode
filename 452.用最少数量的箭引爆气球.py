#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], x[0]))
        cnt = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                cnt += 1
                end = point[1]
        return cnt

# @lc code=end

