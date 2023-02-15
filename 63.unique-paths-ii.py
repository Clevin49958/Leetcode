#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        n += 1
        m += 1
        dp = [[0] * (n) for _ in range(m)]
        dp[0][1] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j-1]:
                    continue
                if i==1 or not obstacleGrid[i-2][j-1]:
                    dp[i][j] += dp[i-1][j]
                if j == 1 or not obstacleGrid[i-1][j-2]:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

# @lc code=end
from util import test_local
test_local(Solution().uniquePathsWithObstacles, [[0,0,0],[0,1,0],[0,0,0]], [[0,0]])

