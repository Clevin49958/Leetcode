#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        ints = '0123456789'
        def trim_int(s: str):
            if len(s) == 0:
                return '', False
            for i in range(len(s)):
                if s[i] not in ints:
                    break
            else:
                return '', True
            return s[i:], i != 0
        if len(s) == 0:
            return False
        if s[0] in '+-':
            s = s[1:]
        s, start_trim = trim_int(s)
        if len(s) == 0:
            return start_trim
        end_trim = False
        if s[0] in '.':
            s, end_trim = trim_int(s[1:])
        if not (start_trim or end_trim):
            return False
        if len(s) == 0:
            return True
        if s[0] not in 'eE':
            return False
        s = s[1:]
        if len(s) == 0:
            return False
        if s[0] in '+-':
            s = s[1:]
        if len(s) == 0:
            return False
        s, trimed = trim_int(s)
        return trimed and len(s) == 0

# @lc code=end
from util import test_local
test_local(Solution().isNumber, "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".")
        

