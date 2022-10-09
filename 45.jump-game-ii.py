#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        reach = [min(i + v, n - 1) for i, v in enumerate(nums)]
        reach_from = [inf] * n
        for i, v in reversed([*enumerate(reach)]):
            reach_from[v] = i
        for i in range(n - 2, 0, -1):
            reach_from[i] = min(reach_from[i], reach_from[i + 1])

        counter = 0
        idx = n - 1
        while idx != 0:
            counter += 1
            idx = reach_from[idx]
        return counter

# @lc code=end
import util
util.test_local(Solution().jump, [2,3,1,1,4])