#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def __init__(self):
        self.temp = []
    
    def merge(self, nums, left, mid, right):
        for i in range(left, right + 1):
            self.temp[i] = nums[i]
        
        p = left
        i, j = left, mid + 1
        for p in range(left, right + 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == right + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
    
    def sort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.sort(nums, left, mid)
        self.sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.temp = [0 for _ in range(len(nums))]
        self.sort(nums, 0, len(nums)-1)
        return nums

# @lc code=end

