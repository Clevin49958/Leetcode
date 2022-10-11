#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
from typing import List
from copy import deepcopy


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

    def totalNQueens(self, n: int) -> List[List[str]]:
        grid = [[False] * n for _ in range(n)]
        sols = []
        self.nQueen(n, 0, grid, sols)
        # q_grid = [
        #     ["".join(map(lambda c: "Q" if c else ".", row)) for row in grid]
        #     for grid in sols
        # ]
        return len(sols)


# @lc code=end
