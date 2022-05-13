#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseRange(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while a != b:
            post = a.next
            a.next = prev
            prev = a
            a = post
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a, b = head, head
        for i in range(k):
            if b is None:
                return head
            b = b.next
        new_head = self.reverseRange(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head

# @lc code=end

