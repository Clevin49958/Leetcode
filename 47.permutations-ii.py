#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import Counter, List

# @lc code=start
from copy import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        lst = []
        tn = len(nums)
        counter = Counter(nums)
        nums, freq = [*zip(*counter.items())]
        choice = [0] * len(nums)
        n = len(nums)

        def recur(level):
            if level == 0:
                ans.append(copy(lst))
                return
            for i in range(n):
                if choice[i] < freq[i]:
                    choice[i] += 1
                    lst.append(nums[i])
                    recur(level - 1)
                    choice[i] -= 1
                    lst.pop()

        recur(tn)
        return ans

# @lc code=end
from util import test_local

test_local(Solution().permuteUnique, [1, 2, 3], [0, 1], [1, 1, 2])
