#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, root, path, target, total):
        if root.left is None and root.right is None:
            if total == target:
                self.ans.append(path[:])
            return
        if root.left is not None:
            total += root.left.val
            self.backtrack(root.left, path + [root.left.val], target, total)
            total -= root.left.val
        if root.right is not None:
            total += root.right.val
            self.backtrack(root.right, path + [root.right.val], target, total)
            total -= root.right.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.ans = []
        self.backtrack(root, [root.val], targetSum, root.val)
        return self.ans
        
# @lc code=end

