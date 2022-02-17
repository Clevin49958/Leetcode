# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        current = start
        while l1 or l2:
            s = current.val
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            current.val = s % 10
            current.next = ListNode(val=s // 10)
            current = current.next
        current = start
        while current.next and current.next.next:
            current = current.next
        if current.next.val == 0:
            current.next = None
        return start

            
l1 = [2,4,5]
l2 = [5, 6, 4]
def nodelise(l: List[int]):
    start = None
    for item in l:
        if not start:
            start = ListNode(item)
            curr = start
        else:
            curr.next = ListNode(item)
            curr = curr.next
    return start

def denodelise(l: Optional[ListNode]):
    result = []
    while l:
        result.append(l.val)
        l = l.next
    return result

ld1 = nodelise(l1)
ld2 = nodelise(l2)

print(denodelise(Solution().addTwoNumbers(ld1, ld2)))
        