#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid) + 1, len(grid[0]) + 1
        dp = [[inf] * n for _ in range(m)]
        dp[0][1] = dp[1][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

from util import test_local
test_local(Solution().minPathSum, [[1,3,1],[1,5,1],[4,2,1]])