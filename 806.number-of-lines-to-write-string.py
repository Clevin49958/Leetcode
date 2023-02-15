#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        pixels = 0
        lines = 0
        for c in s:
            pixel = widths[ord(c) - 0x61]
            pixels += pixel
            if pixels > 100:
                lines += 1
                pixels = pixel
        return [lines + (1 if pixels > 0 else 0), pixels]
# @lc code=end

