#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from math import inf
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def search(node: Optional[TreeNode]):
            sub_l = sub_r = l = r = 0
            neg_r = neg_l = -inf
            if node.left:
                sub_l, l, neg_l = search(node.left)
            if node.right:
                sub_r, r, neg_r = search(node.right)
            return max(sub_l, sub_r, l, r, l + node.val + r), max(0, node.val + max(l, r)), max(neg_l, neg_r, node.val)
        total, _, negativ = search(root)
        return total if total > 0 else negativ
# @lc code=end

