#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from copy import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        choice = set()
        lst = []
        n = len(nums)

        def recur(level):
            if level == 0:
                ans.append(copy(lst))
                return
            for i in range(n):
                if i not in choice:
                    choice.add(i)
                    lst.append(nums[i])
                    recur(level - 1)
                    choice.remove(i)
                    lst.pop()

        recur(n)
        return ans


# @lc code=end
from util import test_local

test_local(Solution().permute, [1, 2, 3], [0, 1], [1])
