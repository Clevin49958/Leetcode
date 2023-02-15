#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes:List[ListNode] = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        n = len(nodes)
        if n == 0:
            return head
        k %= n
        if k == 0:
            return head
        new_head = nodes[-k-1].next
        nodes[-k-1].next = None
        nodes[-1].next = head
        return new_head

        
# @lc code=end

