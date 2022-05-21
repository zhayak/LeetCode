#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[(root_idx+1):]
        left_preorder = preorder[1:(1+len(left_inorder))]
        right_preorder = preorder[(1+len(left_inorder)):(1+len(left_inorder)+len(right_inorder))]
        left_tree = self.buildTree(left_preorder, left_inorder)
        right_tree = self.buildTree(right_preorder, right_inorder)
        root.left = left_tree
        root.right = right_tree
        return root

# @lc code=end

