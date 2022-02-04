# Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_p = res
        carry = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            val3 = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            res_p.next = ListNode(val3)
            res_p = res_p.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry > 0:
            res_p.next = ListNode(carry)

        return res.next
