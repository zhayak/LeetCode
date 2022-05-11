#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pfast = pslow = head
        while pfast is not None and pfast.next is not None:
            pfast = pfast.next.next
            pslow = pslow.next
        return pslow
# @lc code=end

