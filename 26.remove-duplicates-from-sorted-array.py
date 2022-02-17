#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        w = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[w] = nums[i]
                w += 1
        return w

# @lc code=end

