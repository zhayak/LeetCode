#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n)]
        ans = [0 for _ in range(n)]
        for booking in bookings:
            i, j, num = booking
            diff[i - 1] += num
            if j < n:
                diff[j] -= num
        ans[0] = diff[0]
        for i in range(1, n):
            ans[i] = ans[i - 1] + diff[i]
        return ans

# @lc code=end

