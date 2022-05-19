#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def maxDiameterOfNode(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLeft = self.maxDiameterOfNode(root.left)
        maxRight = self.maxDiameterOfNode(root.right)
        self.res = max(self.res, maxLeft + maxRight)
        return 1 + max(maxLeft, maxRight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameterOfNode(root)
        return self.res

# @lc code=end

