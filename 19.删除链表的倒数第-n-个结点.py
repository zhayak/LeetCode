#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pslow = pfast = dummy
        for i in range(n+1):
            pfast = pfast.next
        while pfast is not None:
            pslow = pslow.next
            pfast = pfast.next
        pslow.next = pslow.next.next
        return dummy.next

# @lc code=end

