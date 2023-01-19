#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        # maintain adjacency list
        forward = defaultdict(list)
        backward = defaultdict(list)
        for a, b in edges:
            forward[a].append(b)
            backward[b].append(a)

        # fing the head node
        heads = []
        for k in range(n):
            v = backward[k]
            if len(v) == 0:
                heads.append(k)
        # gurantee loop
        if len(heads) == 0:
            return -1
        print(heads)
        
        # find topolocical order and loop detection with dfs
        # 0: not seen, 1: seen, 2: done
        status = [0] * n
        reverse_order = []
        def topo(node):
            if status[node] == 1:
                # loop detected
                raise OverflowError("cycle")
            if status[node] == 2:
                return
            status[node] = 1
            for neighbor in forward[node]:
                topo(neighbor)
            status[node] = 2
            reverse_order.append(node)
        try:
            for node in range(n):
                topo(node)
        except OverflowError:
            return -1
        # reverse_order = list(reversed(reverse_order))
        print(list(reversed(reverse_order)))

        # dp for max occurence per color per node
        ocurrences = [defaultdict(lambda : 0) for _ in range(n)]
        max_color_value = 0
        for node in reversed(reverse_order):
            color = colors[node]
            occurence = ocurrences[node]
            occurence[color] += 1

            for neighbor in forward[node]:
                neighbor_occurence = ocurrences[neighbor]
                for color, value in occurence.items():
                    neighbor_occurence[color] = max(neighbor_occurence[color], value)
            # check at tail node
            if len(forward[node]) == 0:
                max_color_value = max(max_color_value, *occurence.values())
        return max_color_value

# @lc code=end

import util
util.test_local(
    Solution().largestPathValue,
    ("abaca", [[0,1],[0,2],[2,3],[3,4]]),
    ("a", [[0,0]]),
    ("aaa", [[1,2],[2,1]]),
    expand=True
)