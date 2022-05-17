#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        from random import randint
        self.val_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx1 = self.val_to_index[val]
        idx2 = len(self.nums) - 1
        tmp = self.nums[idx2]
        self.nums[idx2] = self.nums[idx1]
        self.nums[idx1] = tmp
        self.val_to_index[tmp] = idx1
        del self.val_to_index[val]
        self.nums.pop(-1)
        return True

    def getRandom(self) -> int:
        rand_idx = randint(0, len(self.nums) - 1)
        return self.nums[rand_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

