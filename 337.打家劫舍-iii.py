#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
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
        self.memo = {}
    
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root in self.memo:
            return self.memo[root]
        yes = root.val
        if root.left is not None:
            yes += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right is not None:
            yes += self.rob(root.right.left) + self.rob(root.right.right)
        no = self.rob(root.left) + self.rob(root.right)
        ans = max(yes, no)
        self.memo[root] = ans
        return ans

# @lc code=end

