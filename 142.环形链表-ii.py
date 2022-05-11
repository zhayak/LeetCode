#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pfast = pslow = head
        while pfast is not None and pfast.next is not None:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                pres = head
                while True:
                    if pres == pslow:
                        return pres
                    pres = pres.next
                    pslow = pslow.next
        return None
        
# @lc code=end

