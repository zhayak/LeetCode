#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        ans = root
        while root.left is not None:
            pre = root
            while root is not None:
                root.left.next = root.right
                root.right.next = root.next.left if root.next is not None else None
                root = root.next
            root = pre.left
        return ans
        
# @lc code=end

