#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
import re
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mapped = [[] for _ in range(len(s))]
        for word in wordDict:
            for match in re.finditer(f"(?=({word}))", s):
                mapped[match.start()].append(word)
        res = []
        def recur(idx, sentence: List[str]):
            if idx == len(s):
                res.append(' '.join(sentence))
                return
            
            for word in mapped[idx]:
                sentence.append(word)
                recur(idx + len(word), sentence)
                sentence.pop()
        recur(0, [])
        return res
        
# @lc code=end
from util import test_local
test_local(Solution().wordBreak, 
    ("catsanddog", ["cat","cats","and","sand","dog"]),
    ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]),
    ("catsandog", ["cats","dog","sand","and","cat"]),
    ("aaaaaaa", ["aaaa","aaa"]),
    expand=True
)
