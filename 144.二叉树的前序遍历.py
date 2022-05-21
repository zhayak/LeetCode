#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res

# @lc code=end

