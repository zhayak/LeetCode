#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pfast = pslow = head
        while pfast is not None and pfast.next is not None:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow:
                return True
        return False
        
# @lc code=end

