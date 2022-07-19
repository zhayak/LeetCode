#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, start, end):
        if start > end:
            return [None]
        trees = []
        for i in range(start, end + 1):
            left_trees = self.helper(start, i - 1)
            right_trees = self.helper(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n)

# @lc code=end

