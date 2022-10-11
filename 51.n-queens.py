#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from copy import deepcopy
from typing import List


class Solution:
    count = 0

    def valid_up(self, grid, col, level, n):
        # vert
        for i in range(level):
            if grid[i][col]:
                return False
            if col >= (level - i) and grid[i][col - (level - i)]:
                return False
            if col + (level - i) <= (n - 1) and grid[i][col + (level - i)]:
                return False
        return True

    def nQueen(self, n: int, level: int, grid: List[List[str]], sols):
        if level == n:
            sols.append(deepcopy(grid))
            return
        for i in range(n):
            if self.valid_up(grid, i, level, n):
                grid[level][i] = True
                self.nQueen(n, level + 1, grid, sols)
                grid[level][i] = False
        return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[False] * n for _ in range(n)]
        sols = []
        self.nQueen(n, 0, grid, sols)
        q_grid = [
            ["".join(map(lambda c: "Q" if c else ".", row)) for row in grid]
            for grid in sols
        ]
        return q_grid


# @lc code=end

import util

util.test_local(Solution().solveNQueens, 1, 2, 3, 4, 9)
