# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            if target - nums[i] not in res:
                res[nums[i]] = i
            else:
                return [res[target - nums[i]], i]
