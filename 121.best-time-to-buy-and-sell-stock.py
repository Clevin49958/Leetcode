#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mins = [inf] * n
        maxs = [inf] * n
        mins[0], maxs[-1] = prices[0], prices[-1]
        delta = 0
        for i in range(1, n):
            mins[i] = min(mins[i-1], prices[i])
        for i in range(n-2, -1, -1):
            maxs[i] = max(maxs[i+1], prices[i])
        for i in range(n):
            delta = max(delta, maxs[i]-mins[i])
        return delta

# @lc code=end

