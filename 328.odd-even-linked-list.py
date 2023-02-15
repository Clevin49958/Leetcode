#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        oh = o = head
        eh = e = head.next
        while e and e.next:
            to = e.next
            te = to.next
            o.next = to
            e.next = te
            e = e.next
            o = o.next
        o.next = eh
        return oh
        
# @lc code=end

