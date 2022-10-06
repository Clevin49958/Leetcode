#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from cmath import exp
from util import test_local

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def com_recur(
        self, candidates: List[int], counts: List[int], target: int
    ) -> List[List[int]]:
        candidate = candidates.pop()
        if target == 0:
            candidates.append(candidate)
            return [[]]
        if len(candidates) == 0:
            candidates.append(candidate)
            return (
                [[candidate] * (target // candidate)]
                if target % candidate == 0 and (target // candidate) <= counts[-1]
                else None
            )
        res = []
        count = counts.pop()
        for i in range(min(target // candidate + 1, count + 1)):
            temp = self.com_recur(candidates, counts, target - i * candidate)
            if temp:
                for arr in temp:
                    arr.extend([candidate] * i)
                res.extend(temp)

        candidates.append(candidate)
        counts.append(count)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        vals, cnts = [*map(list, zip(*Counter(candidates).items()))]
        res = self.com_recur(vals, cnts, target)
        return res


# @lc code=end

test_local(
    Solution().combinationSum2,
    ([10, 1, 2, 7, 6, 1, 5], 8),
    ([2, 5, 2, 1, 2], 5),
    expand=True,
)
