#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

import re
# @lc code=start


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^[+-]?((\d+)|(\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?$", s) is not None
        
# @lc code=end
from util import test_local
test_local(Solution().isNumber, "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".")
        

