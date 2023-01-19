#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
       moves = Counter(moves)
       return moves['U'] == moves['D'] and moves['L'] == moves['R']
        
# @lc code=end

