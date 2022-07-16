#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root):
        while root.left is not None:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            # case 1: 若节点为末端节点，直接删除即可
            if root.left is None and root.right is None:
                return None
            # case 2: 若只有一侧子树，直接让这个孩子接替自己
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # case 3: 若左右子树都存在，则找到右子树中最小的节点来接替
            else:
                min_node = self.findMin(root.right)
                root.right = self.deleteNode(root.right, min_node.val)
                min_node.left = root.left
                min_node.right = root.right
                root = min_node
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root

# @lc code=end

