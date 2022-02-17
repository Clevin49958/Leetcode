#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        p = head
        c = 0
        while p:
            c+=1
            p = p.next
        p = head
        for _ in range(c // k):
            local_prev = None
            start = p
            for _ in range(k):
                next = p.next
                p.next = local_prev
                local_prev = p
                p = next
            start.next = next
            if start is head:
                head = local_prev              
            else:
                prev.next = local_prev
            
            prev = start
        return head

# @lc code=end

Solution().reverseKGroup(nodelise([1,2,3,4,5]), 2)