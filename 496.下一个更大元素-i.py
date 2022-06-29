#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        mapping = dict(zip(nums1, [_ for _ in range(len(nums1))]))
        ans = [-1 for _ in range(len(nums1))]
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                if stack[-1] in mapping:
                    ans[mapping[stack[-1]]] = num
                stack.pop()
            stack.append(num)
        return ans

# @lc code=end

