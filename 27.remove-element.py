#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[w], w = nums[i], w + 1
        return w
# @lc code=end

