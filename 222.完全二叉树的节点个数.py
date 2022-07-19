#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l, r = root, root
        lh, rh = 0, 0
        while l is not None:
            l = l.left
            lh += 1
        while r is not None:
            r = r.right
            rh += 1
        if lh == rh:
            return 2 ** lh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=end

