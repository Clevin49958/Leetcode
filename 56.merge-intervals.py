#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals.pop(0)]
        for left, right in intervals:
            if left <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], right)
            else:
                res.append([left, right])
        return res
# @lc code=end

