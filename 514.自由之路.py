#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
class Solution:
    def helper(self, ring_dict, ring_len, key, i, j):
        if j == len(key):
            return 0
        if self.memo[i][j] > 0:
            return self.memo[i][j]
        ch = key[j]
        res = ring_len * len(key)
        for idx in ring_dict[ch]:
            step = min((idx - i) % ring_len, (i - idx) % ring_len) + 1
            sub = self.helper(ring_dict, ring_len, key, idx, j + 1)
            res = min(res, sub + step)
        self.memo[i][j] = res
        return res

    def findRotateSteps(self, ring: str, key: str) -> int:
        self.memo = [[0 for _ in range(len(key))] for _ in range(len(ring))]
        ring_dict = {}
        for i in range(len(ring)):
            if ring[i] not in ring_dict:
                ring_dict[ring[i]] = [i]
            else:
                ring_dict[ring[i]].append(i)
        res = self.helper(ring_dict, len(ring), key, 0, 0)
        return res       

# @lc code=end

