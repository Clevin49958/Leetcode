#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

from modulefinder import IMPORT_NAME
from typing import List, Optional

from q19 import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        for lista in lists:
            if not lista:
                continue
            heapq.heappush(heap, (lista.val, idx, lista))
            idx += 1
        head = pointer = ListNode(-1)
        while len(heap):
            val, _, lista = heapq.heappop(heap)
            pointer.next = lista
            pointer = pointer.next
            lista = lista.next
            if lista:
                heapq.heappush(heap, (lista.val, idx, lista))
                idx += 1
        return head.next
# @lc code=end

