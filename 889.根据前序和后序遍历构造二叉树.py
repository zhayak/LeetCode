#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            left_idx = postorder.index(preorder[1])
            left_postorder = postorder[:(left_idx+1)]
            left_preorder = preorder[1:(1+len(left_postorder))]
            right_preorder = preorder[(1+len(left_postorder)):]
            right_postorder = postorder[(left_idx+1):-1]
        else:
            left_preorder, left_postorder, right_preorder, right_postorder = [], [], [], []
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        return root

# @lc code=end

