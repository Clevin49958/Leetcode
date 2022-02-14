#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = {x for x in nums}
        return len(nums) > len(num_set)
        
# @lc code=end

