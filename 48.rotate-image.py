#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = matrix
        t = n - 1
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                m[i][j], m[j][t - i], m[t - i][t - j], m[t - j][i] = (
                    m[t - j][i],
                    m[i][j],
                    m[j][t - i],
                    m[t - i][t - j],
                )


# @lc code=end

import util

util.test_local(
    Solution().rotate, [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
)
