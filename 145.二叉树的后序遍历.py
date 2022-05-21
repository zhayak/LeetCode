#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
        self.res = []

    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res
        
# @lc code=end

