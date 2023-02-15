#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        x,y = -1,0
        dirs = [[1,0, 0],[0,1, -1],[-1,0, -1],[0,-1, -2]]
        v = 1
        m = n
        while v <= m ** 2:
            for dx, dy, steps in dirs:
                for i in range(n + steps):
                    x += dx
                    y += dy
                    mat[y][x] = v
                    v += 1
            n -= 2
        return mat

            

# @lc code=end
from util import test_local
test_local(Solution().generateMatrix, 5,4,1)
