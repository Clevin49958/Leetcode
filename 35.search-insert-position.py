#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from cmath import exp
from util import test_local

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(s, t):
            if s >= t:
                return s if nums[s] >= target else s + 1
            mid = (s + t) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search(s, mid - 1)
            else:
                return search(mid + 1, t)

        return search(0, len(nums) - 1)


# @lc code=end

arr = [1, 3, 5, 6]
test_local(Solution().searchInsert, (arr, 2), (arr, 3), expand=True)
