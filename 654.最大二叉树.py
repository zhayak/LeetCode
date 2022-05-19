#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_num = max(nums)
        max_idx = nums.index(max_num)
        root = TreeNode(max_num)
        left_nums = nums[:max_idx]
        right_nums = nums[(max_idx+1):]
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)
        return root

# @lc code=end

