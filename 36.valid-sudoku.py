#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

from itertools import product
from typing import List
from util import test_local

# @lc code=start
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counter = Counter(row)
            for k, v in counter.items():
                if k != "." and v > 1:
                    return False
        for col in range(9):
            counter = Counter([board[r][col] for r in range(9)])
            for k, v in counter.items():
                if k != "." and v > 1:
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                counter = Counter(
                    [board[i + dx][j + dy] for dx, dy in product(range(3), range(3))]
                )
                for k, v in counter.items():
                    if k != "." and v > 1:
                        return False

        return True


# @lc code=end

test_local(
    Solution().isValidSudoku,
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
)
