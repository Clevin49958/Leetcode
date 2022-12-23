#
# @lc app=leetcode id=1610 lang=python3
#
# [1610] Maximum Number of Visible Points
#

# @lc code=start
from typing import List
from math import pi, atan2


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        n = len(points)
        points = [*filter(lambda p: p!=location, points)]
        angles = [*map(lambda p: atan2(p[1]-location[1], p[0]-location[0]) / pi * 180, points)]
        central = n - len(angles)
        # print(angles)
        angles.sort()
        angles.extend([*map(lambda x: x + 360, angles)])
        left = right = 0
        total = 0
        n = len(angles)
        # print(angles)
        while right < n:
            while right < n and angles[right] - angles[left] <= angle:
                right += 1
            total = max(right - left, total)
            while right < n and angles[right] - angles[left] > angle:
                left += 1
        return total + central


# @lc code=end

from util import test_local
test_local(
    Solution().visiblePoints,
    ([[2,1],[2,2],[3,3]], 90, [1,1]),
    ([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]], 0, [1,1]),
    expand=True
)