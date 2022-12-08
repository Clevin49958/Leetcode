#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        def recur(i, partial):
            if i == len(nums):
                return
            for node in range(i, n):
                if len(partial) == 0 or nums[node] >= partial[-1]:
                    new_p = (*partial, nums[node])
                    if len(new_p) > 1:
                        ans.add(new_p)
                    recur(node + 1, new_p)
        recur(0, ())
        return ans

# @lc code=end
from util import test_local
test_local(
    Solution().findSubsequences,
    [4,6,7,7],
    [1,3,5,7]
)
