#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        adjacency = defaultdict(set)
        if beginWord not in wordList:
            wordList.append(beginWord)
        wordList = set(wordList)
        lw = len(beginWord)
        for word in wordList:
            for i in range(lw):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    worb = word[:i] + c + word[i + 1 :]
                    if worb in wordList:
                        adjacency[word].add(worb)
                        adjacency[worb].add(word)
        if endWord not in adjacency:
            return []
        queue = deque([[beginWord, 0]])
        target_dist = inf
        seen = defaultdict(lambda: inf)
        seen[beginWord] = 0
        pred = defaultdict(list)
        while queue:
            curr, dist = queue.popleft()
            if curr == endWord and dist < target_dist:
                target_dist = dist
            if dist == target_dist:
                continue
            for node in adjacency[curr]:
                if seen[node] > dist:
                    if seen[node] == inf:
                        queue.append([node, dist + 1])
                    seen[node] = dist + 1
                    pred[node].append(curr)

        ans = []

        def recur(curr, path):
            if curr == beginWord:
                ans.append(list(reversed(path)))
            for p in pred[curr]:
                path.append(p)
                recur(p, path)
                path.pop()

        recur(endWord, [endWord])
        return ans


# @lc code=end

from util import test_local

test_local(
    Solution().findLadders,
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
    expand=True,
)
