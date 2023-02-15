#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        remaining_max = [0] * n
        remaining_max[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            remaining_max[i] = max(remaining_max[i + 1], prices[i])
        curr_min = inf
        first_transac = 0
        total = 0
        for i, p in enumerate(prices):
            if p < curr_min:
                curr_min = p
            if p > curr_min:
                first_transac = max(first_transac, p-curr_min)
            total = max(total, first_transac + remaining_max[i] - prices[i]) 
        return total

        
# @lc code=end

# from util import test_local