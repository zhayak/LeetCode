#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dummy = ListNode(0)
        ptmp = dummy
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                ptmp.next = p1
                p1 = p1.next
            else:
                ptmp.next = p2
                p2 = p2.next
            ptmp = ptmp.next
        if p1 is not None:
            ptmp.next = p1
        if p2 is not None:
            ptmp.next = p2
        return dummy.next
# @lc code=end

