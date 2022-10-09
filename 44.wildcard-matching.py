#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        min_l = 0
        new_p = []
        for c in p:
            if c != '*':
                min_l += 1
            if not (c == '*' and len(new_p) > 0 and new_p[-1] == "*"):
                new_p.append(c)
        ns = len(s)
        np = len(new_p)
        p = new_p
        @cache
        def match(sidx, pidx, min_l):
            if sidx == ns:
                return pidx == np or pidx == np - 1 and p[pidx] == '*'
            if pidx == np:
                return False
            if p[pidx] == '*':
                for nsidx in range(sidx, ns + 1 - min_l):
                    if match(nsidx, pidx + 1, min_l):
                        return True
                return False
            elif p[pidx] == '?' or p[pidx] == s[sidx]:
                return match(sidx + 1, pidx + 1, min_l - 1)
            else:
                return False
        return match(0, 0, min_l)
        
            


        
# @lc code=end
from util import test_local
test_local(Solution().isMatch, ("aa", "a"), ("aa", "*"), ("cb", "?a"), ("cb", "?b"), (
    "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
    "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"
), expand=True)