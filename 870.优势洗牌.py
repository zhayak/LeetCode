#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import numpy as np
        sorted1 = list(reversed(sorted(nums1)))
        sorted2 = list(reversed(sorted(nums2)))
        idx_mapping = dict(zip(range(len(nums2)), reversed(np.argsort(nums2))))
        res = [0 for _ in range(len(nums2))]
        for i in range(len(nums2)):
            if sorted1[i] > sorted2[i]:
                res[idx_mapping[i]] = sorted1[i]
            else:
                res[idx_mapping[i]] = sorted1[-1]
                sorted1 = sorted1[:i] + [sorted1[-1]] + sorted1[i:-1]
        return res

# @lc code=end

