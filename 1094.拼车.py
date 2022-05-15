#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for _ in range(1001)]
        for trip in trips:
            num, i, j = trip
            diff[i] += num
            if j + 1 < 1001:
                diff[j] -= num

        total = 0
        for i in range(1001):
            total += diff[i]
            if total > capacity:
                return False
        return True

# @lc code=end

