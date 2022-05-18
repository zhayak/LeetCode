#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        from random import randint
        self.size = n - len(blacklist)
        mapping = {}
        last = n - 1
        for num in blacklist:
            mapping[num] = -1
        for num in blacklist:
            if num >= self.size:
                continue
            while last in mapping:
                last -= 1
            mapping[num] = last
            last -= 1
        self.mapping = mapping

    def pick(self) -> int:
        rand_idx = randint(0, self.size - 1)
        if rand_idx in self.mapping:
            return self.mapping[rand_idx]
        else:
            return rand_idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

