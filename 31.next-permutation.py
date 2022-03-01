#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

from util import insert_sort_local, test_local
# @lc code=start
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1
        print(idx)

        if idx > -1:
            swap_idx = idx + 1
            swap_val = nums[swap_idx]
            for i in range(swap_idx + 1, len(nums)):
                if nums[i] <swap_val and nums[i] > nums[idx]:
                    swap_idx = i
                    swap_val = nums[swap_idx]

            nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
            print(swap_idx, nums)
        
        print(insert_sort_local(nums, start=idx + 1))
        
# @lc code=end

test_local(Solution().nextPermutation, [1,2,3], [1,3,2], [3,1,2], [2,3,1], [5,1,1])
