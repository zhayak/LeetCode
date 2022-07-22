#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def helper(self, n):
        if n < 1:
            return []
        if n == 1:
            return ['0', '1']
        return ['0' + _ for _ in self.helper(n - 1)] + ['1' + _ for _ in self.helper(n - 1)[::-1]]

    def grayCode(self, n: int) -> List[int]:
        return [int(_, 2) for _ in self.helper(n)]
        
# @lc code=end

