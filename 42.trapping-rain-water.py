#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        for i, h in enumerate(height):
            if h == 0:
                continue
            curr_h = 0
            while len(stack) > 0 and stack[-1][1] <= h:
                j, prev_h = stack.pop()
                total += (i - j - 1) * (prev_h - curr_h)
                curr_h = prev_h
            if len(stack) > 0:
                j, prev_h = stack[-1]
                total += (i - j - 1) * (h - curr_h)
            stack.append((i, h))
        return total
            
        
# @lc code=end
from util import test_local
test_local(Solution().trap, [0,1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5])

