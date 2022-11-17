#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#
# @lc code=start
import re
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = re.findall(r'\w+', text)
        total_characters = sum(map(lambda word: len(word), words))
        spaces = len(text) - total_characters
        return (' ' * (spaces // (len(words) - 1))).join(words) + (' ' * (spaces % (len(words) - 1))) if len(words) > 1 else words[0] + spaces * ' '
# @lc code=end

from util import test_local
test_local(Solution().reorderSpaces, "  this   is  a sentence ", " practice   makes   perfect", 'a')