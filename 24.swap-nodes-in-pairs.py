#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
from typing import Optional

from q2 import nodelise, denodelise


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = head
        while p:
            if p.next:
                if p is head:
                    head = p.next
                else:
                    prev.next = p.next
                    prev = p
                next = p.next.next
                p.next.next = p
                p.next = next
                p = p.next
            else:
                p = p.next
        return head
# @lc code=end
Solution().swapPairs(nodelise([2,5,3,4,6,2,2]))

