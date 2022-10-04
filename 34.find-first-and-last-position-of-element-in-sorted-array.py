#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List
from util import test_local

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs_val(nums, s, t, val):
            if s > t:
                return -1
            if nums[s] == val:
                return s
            mid = (s + t) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                return bs_val(nums, s, mid - 1, val)
            else:
                return bs_val(nums, mid + 1, t, val)

        idx = bs_val(nums, 0, len(nums) - 1, target)
        if idx == -1:
            return [-1, -1]

        def bs_upper(s, t, val):
            if s > t:
                return s
            if nums[t] == val:
                return t
            mid = (s + t) // 2 + 1
            if nums[mid] == val:
                return bs_upper(mid, t, val)
            else:
                return bs_upper(s, mid - 1, val)

        def bs_lower(s, t, val):
            if s > t:
                return t
            if nums[s] == val:
                return s
            mid = (s + t) // 2
            if nums[mid] == val:
                return bs_lower(s, mid, val)
            else:
                return bs_lower(mid + 1, t, val)

        upper = bs_upper(idx, len(nums) - 1, target)
        lower = bs_lower(0, idx, target)
        return [lower, upper]


# @lc code=end
test_local(Solution().searchRange, ([5, 7, 7, 8, 8, 10], 8), expand=True)
