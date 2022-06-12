# https://leetcode.cn/problems/univalued-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isUnivalTree(root: TreeNode) -> bool:
        def dfs(curr):
            if not curr:
                return True

            if curr.left:
                if curr.left.val != curr.val or not dfs(curr.left):
                    return False

            if curr.right:
                if curr.right.val != curr.val or not dfs(curr.right):
                    return False

            return True

        return dfs(root)
