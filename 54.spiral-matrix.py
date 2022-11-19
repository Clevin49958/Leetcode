#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix) > 0:
            res.extend(matrix.pop(0))
            if len(matrix) == 0: 
                break
            temp = matrix.pop()
            for row in matrix:
                if len(row) == 0:
                    break
                res.append(row.pop())
            res.extend(reversed(temp))
            for row in reversed(matrix):
                if len(row) == 0:
                    break
                res.append(row.pop(0))
        return res
        
# @lc code=end

from util import test_local
test_local(Solution().spiralOrder, [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])