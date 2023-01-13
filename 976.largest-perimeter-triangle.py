#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
from math import sqrt
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_peri = 0
        for i in range(len(nums) - 1,1,-1):
            a = nums[i]
            for j in range(i - 1, 0, -1):
                b = nums[j]
                if b < a / 2:
                    break
                for k in range(j - 1, -1, -1):
                    c = nums[k]
                    if b + c > a:
                        peri = a + b + c
                        max_peri = max(max_peri, peri)
                        print(f"{a:2} {b:2} {c:2}: {peri:3}")
                        return max_peri
                    else:
                        break
        return max_peri
# @lc code=end

import util
util.test_local(
    Solution().largestPerimeter,
    [2,1,2],
    [1,2,1,10],
    [1,2,3,4,5,6,7,8,9]
)