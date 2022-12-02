#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        prices.append(-1)
        total = 0
        for price in prices:
            l = len(stack)
            if l == 0:
                stack.append(price)
            elif price < stack[-1]:
                if l == 2:
                    total += stack[1] - stack[0]
                stack = [price]
            else:
                if l == 2:
                    stack.pop()
                stack.append(price)
        return total

# @lc code=end

