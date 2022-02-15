#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the loop
        f = s = 0
        s = nums[s]
        f = nums[nums[f]]
        while f != s:
            s = nums[s]
            f = nums[nums[f]]

        # find the entry
        f = 0
        while f != s:
            s = nums[s]
            f = nums[f]
        return f
        

        
# @lc code=end

