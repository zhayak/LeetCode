#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        top = [0 for i in range(len(envelopes))]
        cnt = 0
        for i in range(len(envelopes)):
            num = envelopes[i][1]
            left, right = 0, cnt
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == cnt:
                cnt += 1
            top[left] = num
        return cnt

# @lc code=end

