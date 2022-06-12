# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def sumRootToLeaf(root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if node is None:
                return 0
            val = (val << 1) | node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)


a4 = TreeNode(0)
a5 = TreeNode(1)
a6 = TreeNode(0)
a7 = TreeNode(1)

a2 = TreeNode(0, a4, a5)
a3 = TreeNode(1, a6, a7)
a1 = TreeNode(1, a2, a3)

print(Solution.sumRootToLeaf(a1))