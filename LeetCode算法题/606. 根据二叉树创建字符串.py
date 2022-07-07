# https://leetcode.cn/problems/construct-string-from-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node, ans):
            if not node.left and not node.right:
                return str(node.val)

            if node.left and not node.right:
                return str(node.val) + "(" + dfs(node.left, ans) + ")"

            if not node.left and node.right:
                return str(node.val) + "()" + "(" + dfs(node.right, ans) + ")"

            if node.left and node.right:
                return str(node.val) + "(" + dfs(node.left, ans) + ")" + "(" + dfs(node.right, ans) + ")"

        return dfs(root, "" + str(root.val))