#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the middle of the list
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half of the list
        prev, curr = None, slow.next
        while curr is not None:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        # compare if the two lists are the same
        a, b = head, prev
        while a is not None and b is not None:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True


# @lc code=end

