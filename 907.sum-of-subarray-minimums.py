#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
from collections import Counter, defaultdict
from math import ceil, inf, log
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        mod = 1_000_000_007
        queue = [[0, len(arr)]]
        total = 0

        def build(arr):
            n = len(arr)
            ceiled = 2 ** (ceil(log(n, 2))) - 1
            seg = [inf] * (2 ** (ceil(log(n, 2)) + 1))
            seg[ceiled + 1:ceiled + 1 + len(arr)] = arr
            for i in range(ceiled, 0, -1):
                seg[i] = min(seg[i << 1], seg[(i << 1) + 1])
            return ceiled, seg
        ceiled, seg = build(arr)
        def get_min(l, r, tl=0, tr=ceiled, idx=1):
            nonlocal seg
            if r < tl or l > tr:
                return inf
            if tl >= l and tr <= r:
                return seg[idx]
            return min(get_min(l, r, tl, (tl + tr)//2, idx * 2), get_min(l, r, (tl + tr)//2 + 1, tr, idx * 2 + 1))

        ref = defaultdict(list)
        for i, v in enumerate(arr):
            ref[v].append(i)

        while queue:
            start, end = queue.pop()
            min_val = get_min(start, end - 1)
            prev_idx = start - 1
            n = end - start
            for i in ref[min_val]:
                v = arr[i]
                if v == min_val and i >= start and i < end:
                    total += (i - prev_idx) * (end - i) * v
                    if prev_idx + 1 < i:
                        queue.append([prev_idx + 1, i])
                    prev_idx = i
            if prev_idx + 1 < end:
                queue.append([prev_idx + 1, end])
        return total % mod

# @lc code=end
from util import test_local
import sys

print(sys.setrecursionlimit(30000))
test_local(
    Solution().sumSubarrayMins,
    [3,1,2,4],
    [11,81,94,43,3],
    [3,1]
)
