#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[(root_idx+1):]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):(len(left_inorder)+len(right_inorder))]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
# @lc code=end

