#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def put(self, seq: list, cur: list, start:int, end: int):
        # print(seq, cur, start, end)
        if start == 0 and end == 0:
            seq.append(cur.copy())
        if start > 0:
            cur.append(0)
            self.put(seq, cur, start - 1, end + 1)
            cur.pop()
        if end > 0:
            cur.append(1)
            self.put(seq, cur, start, end - 1)
            cur.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        seq = []
        self.put(seq, [], n, 0)
        def helper(x):
            print(x)
            return '(' if x == 0 else ')'
        seq = [(''.join(map(helper, elem))) for elem in seq]
        return seq

        
# @lc code=end

