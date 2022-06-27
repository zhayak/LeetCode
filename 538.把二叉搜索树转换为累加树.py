#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
        self.curr = 0

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.right)
        self.curr += root.val
        root.val = self.curr
        self.traverse(root.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

# @lc code=end

