#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from itertools import product
from typing import List, Optional


class Solution:
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def tree(start, end):
            if end == start:
                return [TreeNode(start)]
            if end - start == 1:
                return [TreeNode(start, right=TreeNode(end)), TreeNode(end, left=TreeNode(start))]
            res = []
            for v in range(start + 1, end):
                left = tree(start, v-1)
                right = tree(v + 1, end)
                for left_node, right_node in product(left, right):
                    res.append(TreeNode(v, left_node, right_node))

            for head in tree(start + 1, end):
                res.append(TreeNode(start, right=head))
            for head in tree(start, end-1):
                res.append(TreeNode(end, head))
            return res
        return tree(1, n)
        
# @lc code=end

