#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth
        left = self.traverse(root.left, depth + 1)
        right = self.traverse(root.right, depth + 1)
        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

# @lc code=end

