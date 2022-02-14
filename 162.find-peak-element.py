#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start = 0
        end = len(nums) - 1
        while start + 2 <= end:
            mid = (start + end ) // 2
            print(start, end, mid)
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums [mid + 1] > nums[mid]:
                start = mid
            else: 
                end = mid
        print('end', start, end)
        if nums[start] > nums[end]:
            return start
        else:
            return end

# @lc code=end

