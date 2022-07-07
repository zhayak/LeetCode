#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
class Solution:
    def helper(self, indegree, src, curr, k):
        if src == curr:
            return 0
        if k == 0:
            return -1
        if self.memo[curr][k] != -2:
            return self.memo[curr][k]
        res = -1
        if curr in indegree:
            for frm, price in indegree[curr]:
                sub = self.helper(indegree, src, frm, k - 1)
                if sub != -1:
                    res = min(res, sub + price) if res != -1 else sub + price
        self.memo[curr][k] = res
        return res

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        indegree = {}
        for flight in flights:
            frm, to, price = flight
            if to not in indegree:
                indegree[to] = [[frm, price]]
            else:
                indegree[to].append([frm, price])
        self.memo = [[-2 for _ in range(k + 2)] for _ in range(n)]
        res = self.helper(indegree, src, dst, k + 1)
        return res

# @lc code=end
