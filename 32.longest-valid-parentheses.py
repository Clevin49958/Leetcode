#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

from util import test_local
# @lc code=start
import re

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        pairs = [[m.start(), m.end() - 1] for m in re.finditer("\(\)", s)]

        idx = 0
        def expand(pair: list) -> None:
            # expand if follows pattern (((((()))))
            while pair[0] > 0 and pair[1] < len(s) - 1 and s[pair[0] - 1] == '(' and s[pair[1] + 1] == ')':
                pair[0] -= 1
                pair[1] += 1
        
        while idx < len(pairs):
            print(idx, pairs[idx])

            expand(pairs[idx])
            print(idx, pairs[idx])

            # touching previous group e.g. ()((((()))))
            while idx > 0 and pairs[idx - 1][1] + 1 == pairs[idx][0]:
                pairs[idx][0] = pairs[idx-1][0]
                # remove concatenated ones
                del pairs[idx - 1]
                idx -= 1
                expand(pairs[idx])
            print(idx, pairs[idx])

            # update res
            v = pairs[idx][1] - pairs[idx][0] + 1
            if v > res:
                res = v
            print(res)

            idx += 1


        return res
# @lc code=end

test_local(Solution().longestValidParentheses, 
    "(()",
    ")()())",
    "",
    ")(()()(()))())",
    ")(()(()()(()))())"
)
