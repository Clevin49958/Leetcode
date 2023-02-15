#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2: 
            return n
        tail = 0
        next = 1
        curr_count = 1
        while next < n:
            if nums[tail] != nums[next]:
                tail += 1
                nums[tail] = nums[next]
                next += 1
                curr_count = 1
            elif curr_count < 2:
                tail += 1
                nums[tail] = nums[next]
                next += 1
                curr_count += 1
            else:
                next += 1
        return tail + 1
            
# @lc code=end

