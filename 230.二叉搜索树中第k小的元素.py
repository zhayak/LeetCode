#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
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
        self.cnt = 0
        self.ans = None
    
    def traverse(self, root: Optional[TreeNode], k: int):
        if root is None:
            return
        self.traverse(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
            return
        self.traverse(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.ans
        
# @lc code=end

