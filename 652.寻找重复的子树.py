#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
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
        self.subtrees = defaultdict(int)
        self.res = []
    
    def traverse(self, root: Optional[TreeNode]) -> str:
        ans = ""
        if root is None:
            return '#;'
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        ans = str(root.val) + ';' + left + right
        self.subtrees[ans] += 1
        if self.subtrees[ans] == 2:
            self.res.append(root)
        return ans

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res

# @lc code=end

