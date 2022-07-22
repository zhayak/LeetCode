#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        leftTree = self.build(left, mid - 1)
        root = TreeNode(self.curr.val)
        self.curr = self.curr.next
        rightTree = self.build(mid + 1, right)
        root.left = leftTree
        root.right = rightTree
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        self.curr = head
        node = head
        while node is not None:
            length += 1
            node = node.next
        return self.build(0, length - 1)

# @lc code=end

