#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from util import test_local

# @lc code=start
from math import ceil
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidate = candidates.pop()
        if target == 0:
            candidates.append(candidate)
            return [[]]
        if len(candidates) == 0:
            candidates.append(candidate)
            return (
                [[candidate] * (target // candidate)]
                if target % candidate == 0
                else None
            )
        res = []
        for i in range(target // candidate + 1):
            temp = self.combinationSum(candidates, target - i * candidate)
            if temp:
                for arr in temp:
                    arr.extend([candidate] * i)
                res.extend(temp)

        candidates.append(candidate)
        return res


# @lc code=end
test_local(Solution().combinationSum, ([2, 3, 6, 7], 7), ([2, 3, 5], 8), expand=True)
