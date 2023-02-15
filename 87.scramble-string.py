#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from collections import Counter, defaultdict

# construction approach
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        # neighbors = defaultdict(Counter)
        # for i, c in enumerate(s1):
        #     if i > 0:
        #         neighbors[c][s1[i-1]] += 1
        #     if i < len(s1) - 1:
        #         neighbors[c][s1[i + 1]] += 1
        # print(neighbors)
        pass
        blocks = [c for c in s2]
        while len(blocks) > 1:
            n = len(blocks)
            for i in range(n - 1):
                joint = blocks[i] + blocks[i + 1]
                rev_joint = blocks[i + 1] + blocks[i]
                if s1.find(joint) >= 0:
                    # joint = "end"
                    blocks[i] = joint
                    del blocks[i + 1]
                    break
                elif s1.find(rev_joint) >= 0:
                    # joint = "start"
                    blocks[i + 1] = rev_joint
                    del blocks[i]
                    break

            else:
                return False
        return True

# @lc code=end

from util import test_local
test_local(
    Solution().isScramble,
    ("great", "rgeat"),
    ("abcde", "caebd"),
    ("abcdef", "dcaebf"),
    ("abc", "abd"),
    ("abacad", "dcbaaa"),
    ("abca","caba"),
    ("abba", "abab"),
    ("eebaacbcbcadaaedceaaacadccd",
"eadcaacabaddaceacbceaabeccd"),
    expand=True
)
