#
# @lc app=leetcode id=2256 lang=python3
#
# [2256] Minimum Average Difference
#

# @lc code=start
from math import floor, inf
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        n = len(nums)
        r = n
        l = 0
        def section(cum_sum, n):
            return floor(cum_sum/n) if n > 0 else 0
        
        min_v, min_i = inf, -1
        while l < n:
            left += nums[l]
            right -= nums[l]
            l += 1
            r -= 1
            diff =abs(section(left, l) - section(right, r))
            if diff < min_v:
                min_v = diff
                min_i = l - 1
        return min_i

# @lc code=end

