#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverserList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            post = head.next
            head.next = prev
            prev = head
            head = post
        return prev
    
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left_prev, right_curr = dummy, dummy
        for i in range(left-1):
            left_prev = left_prev.next
        for i in range(right):
            right_curr = right_curr.next
        left_curr = left_prev.next
        right_next = right_curr.next
        right_curr.next = None
        self.reverserList(left_curr)
        left_curr.next = right_next
        left_prev.next = right_curr
        return dummy.next

# @lc code=end

