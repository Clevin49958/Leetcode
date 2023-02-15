#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from bisect import bisect_left, insort_left
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort_left(intervals, newInterval, key=lambda arr:arr[0])
        
        res = [intervals.pop(0)]
        for left, right in intervals:
            if left <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], right)
            else:
                res.append([left, right])
        return res
# @lc code=end

