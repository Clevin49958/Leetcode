#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode(-200)
        while list1 or list2:
            if not list2:
                head.next = list1
                list1 = list1.next
            elif not list1 or list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            elif not list2 or list2.val >= list1.val:
                head.next = list1
                list1 = list1.next
            head = head.next
        return res.next


# @lc code=end

print(Solution().mergeTwoLists(ListNode(1), None))