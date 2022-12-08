#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recur(node: Optional[TreeNode], res: List[int]):
            if node is None:
                return res
            if node.left is None and node.right is None:
                res.append(node.val)
                return
            recur(node.left, res)
            recur(node.right, res)
        res1 = []
        recur(root1, res1)
        res2 = []
        recur(root2, res2)
        print(res1, res2)
        return res1 == res2
            
# @lc code=end