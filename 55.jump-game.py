#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = 0
        for i, v in enumerate(nums):
            if i > highest:
                return False
            highest = max(i + v, highest)
        return True
# @lc code=end

from util import test_local
test_local(Solution().canJump,  [2,3,1,1,4], [3,2,1,0,4])