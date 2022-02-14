#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=startclass Solution:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target:
            return 0
        elif nums[end] == target:
            return end
        
        while end - start > 1:
            mid = (start + end) // 2
            print(start, end, mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        return -1
# @lc code=end

